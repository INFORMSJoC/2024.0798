[![INFORMS Journal on Computing Logo](https://INFORMSJoC.github.io/logos/INFORMS_Journal_on_Computing_Header.jpg)](https://pubsonline.informs.org/journal/ijoc)

# The Parallel Epsilon Algorithm for Tri Objective Integer Optimization Problems

This archive is distributed in association with the [INFORMS Journal on
Computing](https://pubsonline.informs.org/journal/ijoc) under the [MIT License](LICENSE).

The software and data in this repository are a snapshot of the software and data
that were used in the research reported on in the paper 
[The Parallel Epsilon Algorithm for Tri Objective Integer Optimization Problems](https://doi.org/10.1287/ijoc.2024.0798) by Kathrin Prinz and Stefan Ruzika. 
The snapshot is based on 
[this SHA](https://github.com/KathrinPrinz/PEA/commit/ec339214a2bbee53430f0413f309e3435b133cd8) 
in the development repository. 

**Important: This code is being developed on an on-going basis at 
https://github.com/KathrinPrinz/PEA. Please go there if you would like to
get a more recent version.**

## Cite

To cite the contents of this repository, please cite both the paper and this repo, using their respective DOIs.

https://doi.org/10.1287/ijoc.2024.0798

https://doi.org/10.1287/ijoc.2024.0798.cd

Below is the BibTex for citing this snapshot of the repository.

```
@misc{prinz2025,
  author =        {Kathrin Prinz and Stefan Ruzika},
  publisher =     {INFORMS Journal on Computing},
  title =         {{The Parallel Epsilon Algorithm for Tri-Objective Integer Optimization Problems}},
  year =          {2025},
  doi =           {10.1287/ijoc.2024.0798.cd},
  url =           {https://github.com/INFORMSJoC/2024.0798},
  note =          {Available for download at https://github.com/INFORMSJoC/2024.0798},
}  
```

## Description

The repository contains a C++ implementation of the Parallel Epsilon Algorithm as described in the corresponding paper. The implementation works for tri-objective integer programs, though, theoretically, the algorithm can be applied to a larger class of problems.

## Usage
The code requires IBM ILOG CPLEX 22.1.1 (or possibly greater), OpenMP 4.5 (or possibly greater) and can be built with cmake. First, adjust the path to CPLEX in the file ```CMakeLists.txt```.
Then, execute
```
cmake CMakeLists.txt
```
and compile with 
```
make
```

The executable is called ```PEA``` and requires the instance file, the results directory and the number of threads that should be used. The instances file needs to be in the LP file format.

### Example
Running 
```
./PEA instances/AP_p-3_n-55_ins-2.lp results/PEA_tutulla/AP_p-3-n-55_ins-2_threads-16.json 16
``` 
will solve the problem specified in the file ```instances/AP_p-3_n-55_ins-2.lp``` and use ```16``` threads. The output will be written to ```results/PEA_tutulla/AP_p-3_n-55_ins-2_threads-16.json```

## Instances 
We use knapsack and assignment instances provided by Kirlik and Sayın [[2]](#2). The orignal upload is no longer available, but the instances can be found under https://github.com/aritrasep/Modolib.jl. To use them with PEA they need to be converted to the LP file format. We additionally generated assignment problem instances of size 55-100 according to their scheme. Those newly generated instances can be found in ```Data```. 

## Benchmark Algorithms
We compared our algorithms to the following algorithms from the literature.  We use CPLEX 22.1.1 as the underlying black-box solver with the parameter MIP gap tolerance set to $10^{-6}$ for all algorithms.

* The Quadrant Shrinking Method (QSM, Boland et al. [[1]](#1)) for tri-objective integer problems. We used the C++ implementation kindly provided to us by the authors.

* The method by Tamby and Vanderpooten (TamVan, [[4]](#4)) for multi-objective discrete optimization problems. We used the Haskell implementation available at https://github.com/tambysatya/TamVan19 and [this SHA](https://github.com/tambysatya/TamVan19/commit/7388e149f24b7a06c676baeaf35ccbe6b08ce955). We followed the instructions and used the Haskell Tool Stack version 2.7.5 and ghc 9.0.2 to compile.

* The Defining Point Algorithm (DPA, Dächert et al. [[3]](#3)). The implementation was obtained from https://github.com/kerstindaechert/DefiningPointAlgorithm and [this SHA](https://github.com/kerstindaechert/DefiningPointAlgorithm/commit/71ec8251c6b556fb7cf47c8a6186e6ee6c8a39ef).

* The Improved Recursive Algorithm (AIRA, Ozlen et al. [[6]](#6)). We used the implementation available at https://github.com/WPettersson/moip_aira and [this SHA](https://github.com/WPettersson/moip_aira/commit/40cd8bff722e227d9bde647f6156ab81da981993) by Petterson and Ozlen [[5]](#5) who parallelized the original algorithm.

Note that the algorithms require different file formats as described in their respective documentation.

## Replicating

We compared the sequential algorithms QSM, DPA and TamVan  and we compare the CPLEX parallelization of QSM, AIRA and PEA on the knapsack and assignment instances. The experiments were performed on a machine with two 2.60 gigahertz Intel Xeon E5-2670 processors, each with 8 physical cores and a RAM size of 188 gigabyte. The operating system was Debian GNU/Linux 12. The C++ algorithms were compiled with gcc 12.2.0.
The python scripts we used to conduct the experiments can be found in the folder ```scripts```. The running time was measured as wall-clock time for all algorithms and it does not include the time spent writing the results to a file. The results can be found in the folders 
AIRA_AP, AIRA_KP, DPA_AP, DPA_KP, PEA_AP, PEA_KP, QSM_AP, QSM_KP, TamVan_AP and TamVan_KP.

We conducted a second round of experiments to further investigate the scaling of PEA. The experiments were performed on another machine with two 3.10 gigahertz AMD EPYC 9554 64-Core processors, 128 cores each and a RAM size of 1511 GiB. The gcc compiler used to complie was 13.2.0. The results can be found in the folder PEA_tutulla.

## References

<a id="1">[1]</a>
Boland, N., Charkhgard, H., Savelsbergh, M. (2017)
The Quadrant Shrinking Method: A simple and efficient algorithm for solving tri-objective integer programs.
European Journal of Operational Research 260(3):873–885

<a id="2">[2]</a>
Kirlik, G., Sayın, S. (2014)
A new algorithm for generating all nondominated solutions of multiobjective discrete optimization problems.
European Journal of Operational Research 232(3):479–488

<a id="3">[3]</a>
Dächert, K., Fleuren, T., Klamroth, K. (2024)
A simple, efficient and versatile objective space algorithm for multiobjective integer programming.
Math. Methods Oper. Res. 100:351-384

<a id="4">[4]</a>
Tamby, S., Vanderpooten, D. (2021)
Enumeration of the nondominated set of multiobjective discrete optimization problems.
INFORMS J. Comput. 33(1):72–85

<a id="5">[5]</a>
Petterson, W., Ozlen M. (2020)
Multiobjective integer programming: Synergistic parallel approaches.
INFORMS J. Comput. 32(2):461–472

<a id="6">[6]</a>
Ozlen, M., Burton, A., Mac Rae, C. A. G. (2024)
Multi-Objective Integer Programming: An Improved Recursive Algorithm.
J. Optim. Theory Appl. 16(2):470-482
