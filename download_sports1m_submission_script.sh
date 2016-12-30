#!/bin/sh
#PBS -N download_Sports1M
#PBS -l select=1:ncpus=24:mem=32GB
#PBS -l walltime=120:00:00
#PBS -q normal
#PBS -j oe
#PBS -o log_job.txt
#PBS -M tranlaman@gmail.com
#PBS -m "e"

cd /home/users/nus/a0081742/Desktop/workspace/sports1m/sports1m-crawler/
bash fetch_sports1m_videos.sh /home/users/nus/a0081742/data/Sports1M_height144 all_vid.txt 20

