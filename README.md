# Hypothetical Lorentz invariance violation and the muon content of extensive air showers
*Nickolay S. Martynenko, Grigory I. Rubtsov, Petr S. Satunin, Andrey K. Sharofeev[^mail], Sergey V. Troitsky*

This repository provides datasets corresponding to the findings presented in [[arXiv:2412.08349]][0]

- [`data/CORSIKA`](data/CORSIKA) — Monte-Carlo dataset produced by the authors utilizing [[CORSIKA-7]][2] EAS simulations
    - [`.../train.json`](data/CORSIKA/train.json) — 'training' MC dataset that was used to fit the heuristic models parameters
    - [`.../test`](data/CORSIKA/test) — 'testing' CSV tables (not employed during the fit) that were used to validate the quality of the fit
- [`data/WHISP.json`](data/WHISP.json) — WHISP meta-analysis [[dataset]][1] that was utilized in our analysis to compare the model predictions with the relevant experimental data assuming various LIV scenarios
- [`utils/read.py`](utils/read.py) — auxiliary python scripts that the reader is encouraged to use in order to easily read JSON files and convert them to python dictionaries for further processing


[0]: <https://arxiv.org/abs/2412.08349> "Nickolay S. Martynenko, Grigory I. Rubtsov, Petr S. Satunin, Andrey K. Sharofeev, Sergey V. Troitsky, 'Hypothetical Lorentz invariance violation and the muon content of extensive air showers' (2024) e-print: arXiv:2412.08349"
[1]: <https://pos.sissa.it/444/466> "J. C. Arteaga Velazquez, 'A report by the WHISP working group on the combined analysis of muon data at cosmic-ray energies above&nbsp;1&nbsp;PeV', PoS ICRC2023, 466 (2023)"
[2]: <https://www.iap.kit.edu/corsika/70.php> "CORSIKA: A Monte Carlo Code to Simulate Extensive Air Showers"

[^mail]: Corresponding author: <a href="mailto:sharofeev@inr.ac.ru?subject=arXiv:2412.08349">sharofeev@inr.ac.ru</a>
