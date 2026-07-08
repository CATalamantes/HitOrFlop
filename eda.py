from pathlib import Path
import pandas as pd

filePath = Path('.') / 'data' / 'youtube_trending_videos_global_daily.parquet'
data = pd.read_parquet(filePath)
print(data.head())
print('Data successfully read!')
print("\n")
################Exploratory Data Analysis
print("==== Exploring Data ====")
print("**DATASET SHAPE")
print(f"Rows: {data.shape[0]}, Columns: {data.shape[1]}\n")

print("**DATA TYPES & MEMORY")
data.info()
print("\n")

print("**MISSING VALUES PER COLUMN")
print(data.isna().sum())
print("\n")

print("**DUPLICATE VALUES")
duplicate_count = data.duplicated().sum()
print(f"Total duplicate rows: {duplicate_count}")
print("\n")

print("**DATA TYPES & MEMORY")
data.info()
print("\n")

print("**STATISTICAL SUMMARY")
print(data.describe())
print("\n")
print("\n")

################Ethical and Bias Finding
print("==== ETHICAL AND BIAS CONSIDERATIONS ====")
print(f"Top Channel Country Values \n {data['channel_country'].value_counts().head(5)}\n")
print(f"Top Video Country Values \n {data['video_trending_country'].value_counts().head(5)}\n")
print(f"Top Video Categories \n {data['video_category_id'].value_counts().head(5)}")
print("\n")
