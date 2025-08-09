import pandas as pd
import os

# File paths
base_path = r"C:\Users\admin\Downloads\Oscar award"
oscars_file = os.path.join(base_path, "Oscar_Winners_Cleaned.csv")
imdb_file = os.path.join(base_path, "Top_1000_IMDB_Movies.csv")

# Read CSV files
oscars_df = pd.read_csv(oscars_file)
imdb_df = pd.read_csv(imdb_file)

# Optional: Strip spaces from column names (good habit)
oscars_df.columns = oscars_df.columns.str.strip()
imdb_df.columns = imdb_df.columns.str.strip()

# Merge datasets on film name and Movie_Title
merged_df = pd.merge(
    oscars_df,
    imdb_df,
    left_on="film",
    right_on="Movie_Title",
    how="inner"
)

# Save merged file
output_file = os.path.join(base_path, "oscars_imdb_cleaned.csv")
merged_df.to_csv(output_file, index=False)

print(f"✅ Merged file saved: {len(merged_df)} rows in {output_file}")
