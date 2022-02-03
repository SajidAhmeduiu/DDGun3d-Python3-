#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --time=0-00:40:00
#SBATCH --mem=40G
#SBATCH --job-name=hhblits_debug 

module purge
# source /dors/meilerlab/data/ahmes10/environments/DDGun_env/bin/activate

/dors/meilerlab/data/ahmes10/DDGun_Run/ddgun/utils/hh-suite/bin/hhblits -d  /dors/meilerlab/data/ahmes10/DDGun_Run/ddgun/data/uniclust30_2018_08/uniclust30_2018_08  -i /ddgun/temporary_data/1aar.pdb.A.fasta -opsi /ddgun/temporary_data/1aar.pdb.A.blastx  -n 1 -cpu 4
