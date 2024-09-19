#!/usr/bin/env bash
export EXTRAE_ENFORCE_FS_SYNC=1
# Configure Extrae
export EXTRAE_CONFIG_FILE=./extrae.xml
# Load the tracing library (choose C/Fortran)
export LD_PRELOAD=$EBROOTEXTRAE/lib/libmpitrace.so
#export LD_PRELOAD=$EBROOTEXTRAE/lib/libmpitracef.so
# Run the program
$*