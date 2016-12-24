Sports1M Tools
=================

Requirements
------------
 1. youtube-dl (https://github.com/rg3/youtube-dl/)

Fetch Sports1M
-----------------
To download all the Sports1M videos run the following command line:
```
    mkdir $VIDEO_PATH
    chmod +x fetch_sports1m_videos.sh
    ./fetch_sports1m_videos.sh $VIDEO_PATH all_vid.txt NUM_WORKERS
```

Where $VIDEO_PATH is the path where the videos will be located. If you already 
have a subset of the videos, input that directory. NUM_WORKERS is the number of
workers to download the dataset concurrently.

Generate all_vid.txt
----------------------
You should download JSON [annotation zip](http://cs.stanford.edu/people/karpathy/deepvideo/sports1m_json.zip) 
from project webpage. Extracting the zip, we have two JSON files: sports1m_train.json and sports1m_test.json. 
Running the following Python script to create all_vid.txt contains Youtube id of all videos of Sports1M:
```
    python generate_all_videos_txt_file.py
```
We have filtered out some videos having excessive duration accoring to recommendations from the [project page]
(http://cs.stanford.edu/people/karpathy/deepvideo/) of the dataset by setting a DURATION THRESHOLD. You can use
the following script to visualize histogram of video durations in Sports1M dataset.
```
    python histogram_durations.py
```