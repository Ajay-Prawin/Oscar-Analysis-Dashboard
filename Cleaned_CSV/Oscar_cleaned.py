import pandas as pd

# Load the data
oscars_path = r"C:\Users\admin\Downloads\Oscar award\Oscar_Winners_Cleaned.csv"
imdb_path = r"C:\Users\admin\Downloads\Oscar award\Top_1000_IMDB_Movies.csv"

oscars_df = pd.read_csv(oscars_path)
imdb_df = pd.read_csv(imdb_path)

# Rename columns to make merging smoother
oscars_df.rename(columns={
    'film': 'Movie_Title',
    'year_film': 'Released_Year'
}, inplace=True)

# Trim whitespaces and make titles lowercase for better matching
oscars_df['Movie_Title'] = oscars_df['Movie_Title'].str.strip().str.lower()
imdb_df['Movie_Title'] = imdb_df['Movie_Title'].str.strip().str.lower()

# Convert Released_Year to numeric just in case
oscars_df['Released_Year'] = pd.to_numeric(oscars_df['Released_Year'], errors='coerce')
imdb_df['Released_Year'] = pd.to_numeric(imdb_df['Released_Year'], errors='coerce')

# Merge both datasets
merged_df = pd.merge(
    oscars_df,
    imdb_df,
    on=['Movie_Title', 'Released_Year'],
    how='inner'
)

# Export merged data for Power BI
output_path = r"C:\Users\admin\Downloads\Oscar award\Oscar_IMDB_Merged.csv"
merged_df.to_csv(output_path, index=False)

print("✅ Merge successful! File saved to:", output_path)
