# Blue Waters "Running Your Jobs" portal page. 

Batch Jobs
Users must submit jobs to the queue in batch mode for normal job runs.

Example scripts are in /sw/userdoc/samplescripts.  A hybrid xe+xk script is also located there showing how to request nodes of both types (xe_xk.pbs ).

If you're using PrgEnv-intel with OpenMP, please see https://bluewaters.ncsa.illinois.edu/intel-compiler for specific recommendations regarding aprun and setting KMP_AFFINITY appropriately.

XE nodes only, packing 1 MPI task per integer core (2 per bulldozer core)

`#!/bin/bash
#IMPORTANT! If above shell isn't the same as your account default shell, add
# the "-i" option to the above line to be able to use "module" commands. 

### set the number of nodes
### set the number of PEs per node
#PBS -l nodes=2048:ppn=32:xe
### set the wallclock time
#PBS -l walltime=01:00:00
### set the job name
#PBS -N testjob
### set the job stdout and stderr
#PBS -e $PBS_JOBID.err
#PBS -o $PBS_JOBID.out
### set email notification
##PBS -m bea
##PBS -M username@host
### In case of multiple allocations, select which one to charge
##PBS -A xyz
### Set umask so users in my group can read job stdout and stderr files
#PBS -W umask=0027

# NOTE: lines that begin with "#PBS" are not interpreted by the shell but ARE
# used by the batch system, wheras lines that begin with multiple # signs,
# like "##PBS" are considered "commented out" by the batch system
# and have no effect.

# If you launched the job in a directory prepared for the job to run within,
# you'll want to cd to that directory
# [uncomment the following line to enable this]
# cd $PBS_O_WORKDIR

# Alternatively, the job script can create its own job-ID-unique directory
# to run within.  In that case you'll need to create and populate that
# directory with executables and perhaps inputs
# [uncomment and customize the following lines to enable this behavior]
# mkdir -p /scratch/sciteam/$USER/$PBS_JOBID
# cd /scratch/sciteam/$USER/$PBS_JOBID
# cp /scratch/job/setup/directory/* .

# To add certain modules that you do not have added via ~/.modules
# use a line like the following (uncommented, of course).  
#module load craype-hugepages2M  perftools

# export APRUN_XFER_LIMITS=1  # to transfer shell limits to the executable

### launch the application
### redirecting stdin and stdout if needed
### NOTE: (the "in" file must exist for input)

aprun -n 65536 ./app.exe  < in > out.$PBS_JOBID

### For more information see the man page for aprun
`

Using XE nodes with MPI and OpenMP (hybrid MPI + OpenMP)
