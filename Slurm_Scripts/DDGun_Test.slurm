#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --time=0-00:40:00
#SBATCH --mem=40G
#SBATCH --job-name=ddgun_test 

module purge
# source /dors/meilerlab/data/ahmes10/environments/DDGun_env/bin/activate
cd /dors/meilerlab/data/ahmes10/DDGun_Run/ddgun

python3 /dors/meilerlab/data/ahmes10/DDGun_Run/ddgun/ddgun_3d.py /dors/meilerlab/data/ahmes10/DDGun_Run/ddgun/test/1aar.pdb A /dors/meilerlab/data/ahmes10/DDGun_Run/ddgun/test/1aar.muts

