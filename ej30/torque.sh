#!/bin/bash
#PBS -l nodes=1:ppn=8,mem=1gb,walltime=00:10:00
#PBS -M ma.henaoa@uniandes.edu.co
#PBS -m abe
#PBS -N Ejercicio30

module load anaconda/python2
export OMP_NUM_THREADS=10
cd $PBS_O_WORKDIR

rm -r serial_files_walk parallel_files_walk
rm -r serial_files_advec parallel_files_advec
rm *.pdf

#advection
gcc -std=c99 nonlinear_advection.c -o nonlinear.x  # serial advection
mkdir serial_files_advec 
cd serial_files_advec
../nonlinear.x
cd ..
rm *.x
gcc -std=c99 -fopenmp nonlinear_advection.c -o nonlinear.x  # parallel advection
mkdir parallel_files_advec 
cd parallel_files_advec
../nonlinear.x
cd ..
python plot_advec.py 
rm *.x

#walk
gcc walk.c -o walk.x  # serial walk
mkdir serial_files_walk 
cd serial_files_walk
../walk.x > walk.txt
cd ..
rm *.x
gcc -fopenmp walk.c -o walk.x  # parallel walk
mkdir parallel_files_walk 
cd parallel_files_walk
../walk.x > walk.txt
cd ..
python plot_walk.py 
rm *.x
