#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --time=0-05:00:00
#SBATCH --mem=60G
#SBATCH --array=1-2
#SBATCH --job-name=ddgun_test 

module purge
# source /dors/meilerlab/data/ahmes10/environments/DDGun_env/bin/activate
cd /dors/meilerlab/data/ahmes10/DDGun_Run/ddgun

#Read a specific line from ```test_filenames```
pdb_filename=$(sed -n "$SLURM_ARRAY_TASK_ID"p /dors/meilerlab/data/ahmes10/DDGun_Run/pdb_names.txt)
muts_filename=$(sed -n "$SLURM_ARRAY_TASK_ID"p /dors/meilerlab/data/ahmes10/DDGun_Run/mut_names.txt)
chain=$(sed -n "$SLURM_ARRAY_TASK_ID"p /dors/meilerlab/data/ahmes10/DDGun_Run/chain_names.txt)

# The chains also have to be read in from some chainsfile
python3 /dors/meilerlab/data/ahmes10/DDGun_Run/ddgun/ddgun_3d.py -p /dors/meilerlab/data/ahmes10/DDGun_Run/SingleChainPDB/${pdb_filename} -c ${chain} -mts /dors/meilerlab/data/ahmes10/DDGun_Run/MutsFiles/${muts_filename} -o /dors/meilerlab/data/ahmes10/DDGun_Run/DDGOutputs/"${pdb_filename}\.outs"

