# DDGun


INTRODUCTION
  DDGun is an untrained method for predicting teh stability change upon mutation


LICENSE

  Copyright (C) 2019  Ludovica Montanucci, Emidio Capriotti 
                      and Piero Fariselli

  This program and all program in this package are free software;
  you can redistribute it and/or modify it under the terms of the
  GNU General Public License as published by the Free Software
  Foundation; either version 2 of the License, or (at your option)
  any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.


CITATION

  Montanucci L, Capriotti E, Frank Y, Ben-Tal N, Fariselli P. (2019).
  DDGun: an untrained method for the prediction of protein stability
  changes upon single and multiple point variations.
  BMC Bioinformatics. 20 (Suppl 14): 335. PMID:31266447


USAGE

    - Run DDGun 3D:
        ./ddgun_3d.py /home/ddgun/test/1aar.pdb A /home/ddgun/test/1aar.muts

        #PDBFILE        CHAIN   VARIANT S_DDG   T_DDG
        1aar.pdb        A       K6A     0.4     0.4
        1aar.pdb        A       T7A     -0.3    -0.3
        1aar.pdb        A       L8A     -0.4    -0.4
        1aar.pdb        A       T9A,G10A        -0.1,-0.1       -0.1


    - Run DDGun Seq:
        ./ddgun_seq.py /home/ddgun/test/1aar.pdb.A.fasta /home/ddgun/test/1aar.muts

        #SEQFILE        VARIANT S_DDG   T_DDG
        1aar.pdb.A.fasta        K6A     0.4     0.4
        1aar.pdb.A.fasta        T7A     -0.5    -0.5
        1aar.pdb.A.fasta        L8A     -1.2    -1.2
        1aar.pdb.A.fasta        T9A,G10A        -0.7,-0.6       -0.7
