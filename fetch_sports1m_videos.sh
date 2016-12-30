#!/bin/bash

SCRIPT_NAME="$0"
if [ $# != 3 ]; then
	echo 'The arguments for the program are not correct!'
	printf 'Usage: %s video_path all_vid_txt_file num_workers\n' $SCRIPT_NAME
	exit
fi

VIDEOPATH=$1
ANN_FILE=$2 	#annotation file
NUM_WORKERS=$3
TIME_STAMP=$(date +%d.%H%M%S)
OUTFILE_PREFIX=$(printf 'cmd_list_%s' $TIME_STAMP)

if [ -d $VIDEOPATH ]; then
    python run_crosscheck.py --video_path=$VIDEOPATH --ann_file=$ANN_FILE --num_workers=$NUM_WORKERS \
    --outfile_prefix=$OUTFILE_PREFIX
else
    echo "Video directory does not exists."
    exit 0
fi

# execute bash file
for i in `seq 1 $NUM_WORKERS`; do
	CMD_FILE_NAME=$(printf "%s_worker%d.txt" $OUTFILE_PREFIX $((i-1)))
	printf 'running %s\n' $CMD_FILE_NAME
	bash $CMD_FILE_NAME &
done

wait

#rm $CMD_FILE_NAME
for i in `seq 1 $NUM_WORKERS`; do
	CMD_FILE_NAME=$(printf "%s_worker%d.txt" $OUTFILE_PREFIX $((i-1)))
	printf 'running %s\n' $CMD_FILE_NAME
	rm $CMD_FILE_NAME
done
echo "Have a good day!"
