from io import StringIO
import json
import numpy as np
import pandas as pd


def read_CORSIKA(fp) -> dict:
    """
    Reads CORSIKA training dataset from json file
    
    Parameters
    ----------
    fp : str
        path to WHISP.json file

    Returns
    -------
    dataset : dict
        A dictionary, where the keys encode the mass scale
        of the LIV model, lg[MLIV / GeV], and the values
        are dictionaries. In these sub-dictionaries, the
        keys are tuples encoding primary particle type 
        (mass number, atomic number) and the values are 
        pandas dataframes. Columns: lg[primary energy / GeV];
        number of electrons of energy >= 1 MeV at the sea level
        (mean and standard error over 100 simulated EASs);
        number of muons of energy >= 1 GeV at the sea level
        (mean and standard error over 100 simulated EASs).
    """
    with open(fp, 'r') as f:
        dataset = json.load(f)
    dataset = {float(key): {
        tuple(entry['(A, Z)']):
        pd.read_json(StringIO(entry['data'])).astype(np.float32)
        for entry in val
    } for key, val in dataset.items()}
    return dataset

def read_WHISP(fp:str) -> dict:
    """
    Reads WHISP dataset [1] from json file
    
    [1]: A report by the WHISP working group on the 
         combined analysis of muon data at cosmic-ray energies 
         above 1 PeV. J.C. Arteaga Velazquez, ICRC2023.
         doi.org/10.22323/1.444.0466
    
    Parameters
    ----------
    fp : str
        path to WHISP.json file

    Returns
    -------
    dataset : dict
        A dictionary, where the keys encode dataset names (in consistency
        with that assigned in [1]) and the values are pandas dataframes.
        Columns: lg[reconstructed energy / GeV], z-scale, z-scale error.
    """
    with open(fp, 'r') as f:
        dataset = json.load(f)
    dataset = {
        name: pd.read_json(data)
        for name, data in dataset.items()
    }
    return dataset

