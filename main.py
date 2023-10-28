import pandas as pd
import matplotlib.pyplot as plt

# read the data from csv file
df = pd.read_csv('imdb_top_1000.csv')


# setting the Series_Title as the index
df.set_index('Series_Title', inplace=True)

# convert 'Released_Year' to numeric value , setting errors='coerce' will convert non-numeric values to NaN
df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')

# filter based on 2 parameters
# filtering movies released after the year 2000 with an IMDB rating greater than 8
filtered_df = df[(df['Released_Year'] > 2000) & (df['IMDB_Rating'] > 8)]
print(filtered_df)

# sort the table using 2 parameters
# sorting by Released_Year and then by IMDB_Rating
sorted_df = df.sort_values(by=['Released_Year', 'IMDB_Rating'], ascending=[False, False])

# statistical functions for the IMDB_Rating column
mean_rating = df['IMDB_Rating'].mean()
std_dev_rating = df['IMDB_Rating'].std()
median_rating = df['IMDB_Rating'].median()
min_rating = df['IMDB_Rating'].min()
max_rating = df['IMDB_Rating'].max()

# building 2 different types of graphs below

# bar chart: displaying  the top 10 genres
df['Genre'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Movie Genres')
plt.ylabel('Number of Movies')
plt.show()

# line chart: showing IMDB ratings over the dataset
df['IMDB_Rating'].plot(kind='line')
plt.title('IMDb Ratings of Top 1000 Movies')
plt.ylabel('Rating')
plt.xlabel('Movie Rank')
plt.show()