# **IMDb Top 1000 Movies Analysis**

This project involves analyzing the IMDb Top 1000 Movies dataset. The dataset provides various details about the movies, such as their titles, release year, IMDb rating, genre, director, leading stars, and more.

## 📊 **Dataset**

The dataset, `imdb_top_1000.csv`, contains the following columns:

- **`Poster_Link`**: Link to the movie's poster.
- **`Series_Title`**: Title of the movie.
- **`Released_Year`**: Year when the movie was released.
- **`Certificate`**: Age certificate of the movie.
- **`Runtime`**: Duration of the movie.
- **`Genre`**: Genre(s) of the movie.
- **`IMDB_Rating`**: IMDb rating of the movie.
- **`Overview`**: Brief description/overview of the movie.
- **`Meta_score`**: Metascore of the movie.
- **`Director`**: Director of the movie.
- **`Star1`**, **`Star2`**, **`Star3`**, **`Star4`**: Leading stars of the movie.
- **`No_of_Votes`**: Number of votes the movie received on IMDb.
- **`Gross`**: Gross earnings of the movie.

## 🔍 **Analysis Overview**

The project performs the following operations on the dataset:

1. **Data Loading**: Loads the data from the CSV file into a Pandas DataFrame.
2. **Index Assignment**: Sets the movie title as the index for easy referencing.
3. **Data Filtering**: Filters movies released after the year 2000 with an IMDb rating greater than 8.
4. **Sorting**: Sorts movies by release year and IMDb rating.
5. **Statistics**: Computes basic statistics (mean, median, standard deviation, etc.) for the IMDb ratings.
6. **Visualization**:
   - **Bar Chart**: Displays the top 10 genres.
   - **Line Chart**: Visualizes IMDb ratings across the top 1000 movies.

## **Setup and Usage**

1. Ensure you have Python and the necessary libraries installed (pandas, matplotlib).
2. Clone this repository or download the project files.
    ```bash
   git clone https://github.com/LashVS/Quiz1.git
3. Run the analysis script:
   ```bash
   python imdb_analysis.py
