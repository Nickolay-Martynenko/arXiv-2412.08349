# Hypothetical Lorentz invariance violation and the muon content of extensive air showers
*Nickolay&nbsp;S.&nbsp;Martynenko<sup>&nbsp;a,&nbsp;b</sup>, Grigory&nbsp;I.&nbsp;Rubtsov<sup>&nbsp;b,&nbsp;a</sup>, Petr&nbsp;S.&nbsp;Satunin<sup>&nbsp;b,&nbsp;a</sup>, Andrey&nbsp;K.&nbsp;Sharofeev<sup>&nbsp;a,&nbsp;b</sup> [^mail], Sergey&nbsp;V.&nbsp;Troitsky<sup>&nbsp;b,&nbsp;a</sup>*

*a.&nbsp;Lomonosov Moscow State University, 1-2&nbsp;Leninskie Gory, Moscow&nbsp;119991, Russia*

*b.&nbsp;Institute for&nbsp;Nuclear Research of&nbsp;the&nbsp;Russian Academy of&nbsp;Sciences, 60th&nbsp;October Anniversary Prospect&nbsp;7a, Moscow&nbsp;117312, Russia*

    @article{Martynenko:2024rhj,
        author = "Martynenko, Nickolay S. and Rubtsov, Grigory I. and Satunin, Petr S. and Sharofeev, Andrey K. and Troitsky, Sergey V.",
        title = "{Hypothetical Lorentz invariance violation and the muon content of extensive air showers}",
        eprint = "2412.08349",
        archivePrefix = "arXiv",
        primaryClass = "astro-ph.HE",
        reportNumber = "INR-TH-2024-023",
        doi = "10.1103/PhysRevD.111.063010",
        journal = "Phys. Rev. D",
        volume = "111",
        number = "6",
        pages = "063010",
        year = "2025"
    }

---

This repository provides datasets corresponding to the findings presented in [[arXiv:2412.08349]][0]

- [`data/CORSIKA`](data/CORSIKA) — Monte-Carlo dataset produced by the authors utilizing [[CORSIKA&nbsp;7]][2] EAS simulations
    - [`.../train.json`](data/CORSIKA/train.json) — 'training' MC dataset that was used to fit the heuristic models parameters
    - [`.../test`](data/CORSIKA/test) — 'testing' CSV tables (not employed during the fit) that were used to validate the quality of the fit
- [`data/WHISP.json`](data/WHISP.json) — WHISP meta-analysis [[dataset]][1] that was utilized in our analysis to compare the model predictions with the relevant experimental data assuming various LIV scenarios
- [`utils/read.py`](utils/read.py) — auxiliary python scripts that the reader is encouraged to use in order to easily read JSON files and convert them to python dictionaries for further processing


[0]: <https://arxiv.org/abs/2412.08349> "Nickolay S. Martynenko, Grigory I. Rubtsov, Petr S. Satunin, Andrey K. Sharofeev, Sergey V. Troitsky, 'Hypothetical Lorentz invariance violation and the muon content of extensive air showers' (2024) e-print: arXiv:2412.08349"
[1]: <https://pos.sissa.it/444/466> "J. C. Arteaga Velazquez, 'A report by the WHISP working group on the combined analysis of muon data at cosmic-ray energies above&nbsp;1&nbsp;PeV', PoS ICRC2023, 466 (2023)"
[2]: <https://www.iap.kit.edu/corsika/70.php> "CORSIKA: A Monte Carlo Code to Simulate Extensive Air Showers"

[^mail]: Corresponding author: [sharofeev@inr.ac.ru](mailto:sharofeev@inr.ac.ru?subject=arXiv:2412.08349)
