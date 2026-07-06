from pathlib import Path
from datetime import timedelta
import re
import pandas as pd

filePath = Path('.') / 'data' / 'youtube_trending_videos_global_daily.parquet'
data = pd.read_parquet(filePath)
print(data.head())
print('Data successfully read!')
print("\n")
################DATA CLEANING

print("==== DATA CLEANING ====")
data_clean = data.dropna()
print(f"Original rows: {data.shape[0]} | Clean rows: {data_clean.shape[0]}")

#####Converting date strings to Date object
data_clean['video_published_at'] = pd.to_datetime(data_clean['video_published_at'])
data_clean['video_trending__date'] = pd.to_datetime(data_clean['video_trending__date'])
#data_clean['channel_published_at'] = pd.to_datetime(data_clean['channel_published_at'])

#####Converting video duration to datetime object
pattern = re.compile(r'P(?:(?P<days>\d+)D)?T?(?:(?P<hours>\d+)H)?(?:(?P<minutes>\d+)M)?(?:(?P<seconds>\d+)S)?')


def regex_parse_duration(val):
    if pd.isna(val) or not isinstance(val, str):
        return pd.NaT

    match = pattern.match(val)
    if not match:
        return pd.NaT

    # Extract matching groups and filter out None values
    time_params = {k: int(v) for k, v in match.groupdict().items() if v}
    return timedelta(**time_params)

data_clean['video_duration_new'] = data_clean['video_duration'].apply(regex_parse_duration)

