def solution():
    # Calculate the number of times Timothy went to the movies in 2010
    timothy_2010 = 24 + 7  # Timothy went to the movies 7 more times in 2010 than in 2009

    # Calculate the number of times Theresa went to the movies in 2010 and 2009
    theresa_2009 = 24 / 2  # In 2009, Theresa saw half as many movies as Timothy did
    theresa_2010 = 2 * timothy_2010  # In 2010, Theresa went to see twice as many movies as Timothy did

    # Calculate the total number of movies Timothy and Theresa saw in 2009 and 2010
    total_movies = 24 + timothy_2010 + theresa_2009 + theresa_2010
    result = total_movies
    return result

print(solution())