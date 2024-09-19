#!/bin/bash
#
#SBATCH --job-name=dice3
#SBATCH --error=%x-%j.e
#SBATCH --output=%x-%j.o
#SBATCH --ntasks=64
#SBATCH --cpus-per-task=1
#SBATCH --time=1:00:00
#SBATCH --account=ap_calcua_staff

ml Python
ml mpi4py
ml SciPy-bundle
# ml matplotlib
# ml CMake
# ml numba
ml Extrae/4.0.4-gompi-2022a
ml

export TRACE_NAME=dice3.prv
srun ./trace.sh python ./dice3.py