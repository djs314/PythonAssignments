## File: ds4ua-assignment-9-solns.py
## Topic: Assignment 9 Solutions
## Name: David Smith
## Section Time: 5:00-6:15
## Grading Group: 5


import pandas as pd # Load pandas as pd
import numpy as np # Load numpy as np
import re # Import the regular expressions library

## 1.

reviews = pd.read_csv('reviews.txt',
                      sep='\t',
                      header=None,
                      names=['Reviewer','Movie','Rating','Time'])
# Read in the reviews DataFrame

reviewer_gp = reviews['Rating'].groupby(reviews['Reviewer']) # Group the dates by
# each reviewer
five_reviewers = reviewer_gp.count().sort_values(ascending=False).index[0:5]
# Get the five reviewers who had the most reviews
top5_reviews = reviews['Rating'].loc[reviews['Reviewer'].isin(five_reviewers)]
# Get the ratings for the top 5 reviewers
top5_ave = top5_reviews.mean() # Get the mean of the reviews from the top 5 reviewers
top5_n = len(top5_reviews) # Count the number of reviews from the top 5 reviewers
top5_s = np.std(top5_reviews, ddof=1) # Get the SD of the reviews from the top 5 reviewers
lower = top5_ave - 1.96*top5_s/(top5_n**0.5) # Get the lower bound of the CI
upper = top5_ave + 1.96*top5_s/(top5_n**0.5) # Get the upper bound of the CI
other_reviews = reviews['Rating'].loc[~reviews['Reviewer'].isin(five_reviewers)]
# Get the ratings for the remaining reviewers
other_ave = other_reviews.mean() # Get the mean of the reviews from the other reviewers
print('The confidence interval is (%f, %f).' % (lower, upper))
print('The mean of the remeaining reviewers is %f.' % other_ave)

"""
# 1
The confidence interval is (2.904859, 2.997580).
The mean of the remeaining reviewers is 3.548470.
The average is not within the confidence interval, indicating that the remaining
reviewers give higher ratings.
"""

## 2.

genres = pd.read_csv('genres.txt',
                     sep='|',
                     header=None,
                     names=['Movie','Title','Date','Video Date','URL','unknown','Action',
                            'Adventure','Animation','Childrens','Comedy','Crime',
                            'Documentary','Drama','Fantasy','FilmNoir','Horror','Musical',
                            'Mystery','Romance','SciFi','Thriller','War','Western'])
# Read in the genres DataFrame
reviews = pd.merge(reviews, genres) # Merge the reviews and genres DataFrames by Movie ID
reviews['Title'].value_counts()[0:10] # Report the top 10 movies by title and the number
# of times each was reviewed

"""
# 2
Star Wars (1977)                 583
Contact (1997)                   509
Fargo (1996)                     508
Return of the Jedi (1983)        507
Liar Liar (1997)                 485
English Patient, The (1996)      481
Scream (1996)                    478
Toy Story (1995)                 452
Air Force One (1997)             431
Independence Day (ID4) (1996)    429
Name: Title, dtype: int64
"""

## 3.

genres_rev = reviews.loc[:, 'Action':'Western'] # Get the genres portion of the DataFrame
genre_c = genres_rev.sum(axis=0) # Add up the columns of the genres, counting them
max_g = genre_c.sort_values(ascending=False).index[0] # Get the most common genre
min_g = genre_c.sort_values().index[0]# Get the least common genre
print('The most common genre is %s, and the least common is %s.' % (max_g, min_g))

"""
# 3
The most common genre is Drama, and the least common is Documentary.
"""

## 4.

genre_r = genres_rev.sum(axis=1) # Add up the rows of the genres, counting the genres
# per review
num2 = len(genre_r[genre_r > 1]) # Count the number of reviews classified in more than
# one genre
perc = (num2/len(reviews))*100 # Calculate the percentage of reviews classified in
# more than one genre
print('%f percent of reviews are for movies classified in at least two genres.' % perc)

"""
# 4
69.938000 percent of reviews are for movies classified in at least two genres.
"""

## 5.

reviewers = pd.read_csv('reviewers.txt',
                        sep='|',
                        header=None,
                        names=['Reviewer','Age','Gender','Occupation', 'Zip Code'])
# Read in the reviewers DataFrame
reviews = pd.merge(reviews, reviewers) # Merge the reviews DataFrame with the reviewers
# DataFrame based on reviewer
male_rev = reviews[reviews['Gender'] == 'M'] # Get the reviews made by men
female_rev = reviews[reviews['Gender'] == 'F'] # Get the reviews made by women
male_ave = male_rev['Rating'].mean() # Get the average review from men
female_ave = female_rev['Rating'].mean() # Get the average review from women
male_n = len(male_rev) # Get the number of reviews from men
female_n = len(female_rev) # Get the number of reviews from women
male_s = np.std(male_rev['Rating'], ddof=1) # Get the SD of the reviews from men
female_s = np.std(female_rev['Rating'], ddof=1) # Get the SD of the reviews from women
male_lower = male_ave - 1.96*male_s/(male_n**0.5) # Get the lower bound of the CI for men
male_upper = male_ave + 1.96*male_s/(male_n**0.5) # Get the upper bound of the CI for men
female_lower = female_ave - 1.96*female_s/(female_n**0.5) # Get the lower bound of the CI for
# women
female_upper = female_ave + 1.96*female_s/(female_n**0.5) # Get the upper bound of the CI for
# women
print('The confidence interval for the average rating of male reviewers is (%f, %f).' %
      (male_lower, male_upper))
print('The confidence interval for the average rating of female reviewers is (%f, %f).' %
      (female_lower, female_upper))

"""
# 5
The confidence interval for the average rating of male reviewers is (3.521309, 3.537269).
The confidence interval for the average rating of female reviewers is (3.517202, 3.545812).
"""

## 6.

zip_c = pd.read_csv('zipcodes.txt',
                    usecols = [1,4],
                    converters={'Zipcode':str}).drop_duplicates()
# Read the relevant zip code data into a DataFrame, ignoring duplicates

zip_ser = pd.Series(data=zip_c['State'].values, index=zip_c['Zipcode'])
# Get a Series with zip codes as the index and states/territories as the values

def ziptostate(code): # A function that takes a zip code as input and return the state,
# territory, Canada, or unknown
    if re.search('[a-zA-Z]+', code): # If the zip code contains a letter, return 'Canada'
        return('Canada')
    elif code in zip_ser.index: # If the zip code does not contain a letter and is in
    # the list, look up the state and return it
        return(zip_ser[code])
    else: # Otherwise, return 'Unknown'
        return('Unknown')

states = reviewers['Zip Code'].apply(ziptostate) # Get a list of the states corresponding
# to the zip codes
reviewers['State'] = states # Add the states as a column to the reviewers DataFrame
reviews = pd.merge(reviews, reviewers) # Merge the reviews and reviewers DataFrames,
# adding the state to reviews
reviews['State'].value_counts()[0:10] # Report the top 10 states and their number of reviews

"""
# 6
CA    13842
MN     7635
NY     6882
IL     5740
TX     5042
OH     3475
PA     3339
MD     2739
VA     2590
MA     2584
Name: State, dtype: int64
"""

## 7.

occ_gp = reviews['Rating'].groupby(reviews['Occupation']) # Group the reviews data
# by occupation
occ_ave = occ_gp.apply(np.mean) # Get the average rating for each occupation
occ_sort = occ_ave.sort_values() # Sort the average ratings from smallest to largest
occ_drop = occ_sort.drop('other', axis=0) # Drop the 'other' occupation row
occ_drop = occ_drop.drop('none', axis=0) # Drop the 'none' occupation row
low = occ_drop.index[0] # Get the occupation with the lowest average review
high = occ_drop.index[-1] # Get the occupation with the highest average review
print('The occupation that gave the highest average review is %s.' % high)
print('The occupation that gave the lowest average review is %s.' % low)

"""
# 7
The occupation that gave the highest average review is lawyer.
The occupation that gave the lowest average review is healthcare.
"""

## 8.

movie_rev = reviews['Movie'].value_counts() # Get a Series of counts for how many times
# each movie was reviewed
movie_rev = movie_rev.sort_values() # Sort the counts from smallest to largest
movie_gp = movie_rev.groupby(movie_rev) # Group the counts by their different values
movies = 100 * movie_gp.count() / len(movie_rev) # Get the number of times that a movie
# was reviewed exactly n times for all n, and use it to calculate the percentages
movies[0:20] # Print the percentage of movies that were reviewed exactly n times, n = 1 to 20

"""
# 8
Movie
1     8.382878
2     4.042806
3     3.567182
4     3.804994
5     3.032105
6     2.318668
7     2.615933
8     1.783591
9     1.961950
10    1.961950
11    1.189061
12    1.664685
13    1.486326
14    0.832342
15    1.307967
16    1.129608
17    0.594530
18    1.426873
19    1.070155
20    0.713436
Name: Movie, dtype: float64
"""

## 9.

totals = reviews.loc[:, 'Action':'Western'].multiply(reviews['Rating'], axis='index')
# Multiply all of the genre columns by the review column
num_g = reviews.loc[:, 'Action':'Western'].sum(axis=0) # Add up the genre columns to get
# the number of reviews in each genre
total_sums = totals.sum(axis=0) # Add up the columns of totals to get the total review
# amount for each genre
total_ave = total_sums / num_g # Get the average review of each genre
total_sort = total_ave.sort_values() # Sort the average reviews of each genre from smallest
# to largest
low_g = total_sort.index[0] # Get the genre with the lowest average review
high_g = total_sort.index[-1] # Get the genre with the highest average review
print('The genre with the highest average review is %s.' % high_g)
print('The genre with the lowest average review is %s.' % low_g)

"""
# 9
The genre with the highest average review is FilmNoir.
The genre with the lowest average review is Fantasy.
"""

## 10a.

f_n = len(reviews[reviews['Gender'] == 'F']) # Count the number of reviews by women
m_n = len(reviews[reviews['Gender'] == 'M']) # Count the number of reviews by men
f_prop = len(reviews[(reviews['Gender'] == 'F') & (reviews['Rating'] >= 4)]) / f_n
# Get the proportion of positive reviews by women
m_prop = len(reviews[(reviews['Gender'] == 'M') & (reviews['Rating'] >= 4)]) / m_n
# Get the proportion of positive reviews by men
lower = (f_prop - m_prop) - 1.96*(((f_prop*(1-f_prop)/f_n) + (m_prop*(1-m_prop)/m_n))**0.5)
# Get the lower bound of the CI
upper = (f_prop - m_prop) + 1.96*(((f_prop*(1-f_prop)/f_n) + (m_prop*(1-m_prop)/m_n))**0.5)
# Get the upper bound of the CI
print('The confidence interval is (%f, %f).' % (lower, upper))

"""
# 10a
The confidence interval is (-0.005766, 0.008327).
Since the confidence interval contains 0, there is not evidence that the proportions differ.
"""

## 10b.

c_n = len(reviews[reviews['State'] == 'Canada']) # Count the number of reviews by Canadians
a_n = len(reviews[reviews['State'] != 'Canada']) # Count the number of reviews by Americans
c_prop = len(reviews[(reviews['State'] == 'Canada') & (reviews['Rating'] >= 4)]) / c_n
# Get the proportion of positive reviews by Canadians
a_prop = len(reviews[(reviews['State'] != 'Canada') & (reviews['Rating'] >= 4)]) / a_n
# Get the proportion of positive reviews by Americans
lower = (c_prop - a_prop) - 1.96*(((c_prop*(1-c_prop)/c_n) + (a_prop*(1-a_prop)/a_n))**0.5)
# Get the lower bound of the CI
upper = (c_prop - a_prop) + 1.96*(((c_prop*(1-c_prop)/c_n) + (a_prop*(1-a_prop)/a_n))**0.5)
# Get the upper bound of the CI
print('The confidence interval is (%f, %f).' % (lower, upper))

"""
# 10b
The confidence interval is (-0.067761, -0.024404).
Since the confidence interval is below 0, there is actually evidence that Canadians give
more negative reviews.
"""