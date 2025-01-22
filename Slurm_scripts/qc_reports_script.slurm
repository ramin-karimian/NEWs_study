#!/bin/bash

#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40
#SBATCH --cpus-per-task=1
#SBATCH --mem=120gb
#SBATCH --job-name="job1_qc_reports_script"
#SBATCH --account=st-spakpour-1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=raminkarimiangh@gmail.com
#SBATCH --output=/scratch/st-spakpour-1/NEWs_study/Slurm_scripts/logfiles/qc_reports_script_slurm_output.log
#SBATCH --error=/scratch/st-spakpour-1/NEWs_study/Slurm_scripts/logfiles/qc_reports_script_slurm_error.log

################################################################################

cd  /scratch/st-spakpour-1/NEWs_study

source activate /scratch/st-spakpour-1/envs/qc
python qc_reports_script.py



