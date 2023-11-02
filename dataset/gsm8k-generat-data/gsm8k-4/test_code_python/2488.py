def solution():
    """Timothy and Theresa go to the movies very often. Timothy went to the movies 7 more times in 2010 that he did in 2009. In 2009, Timothy went to the movies 24 times. In 2010 Theresa went to see twice as many movies as Timothy did, but in 2009, she only saw half as many as he did. How many movies did Timothy and Theresa go on in both 2009 and 2010?"""
    # Calculate the number of times Timothy went to the movies in 2010
    timothy_2010 = 24 + 7

    # Calculate the number of times Theresa went to the movies in 2010
    theresa_2010 = timothy_2010 * 2

    # Calculate the number of times Timothy and Theresa went to the movies in 2009
    total_2009 = 24 + 12  # 12 as Theresa saw half as many movies as Timothy did in 2009

    # Calculate the number of times Timothy and Theresa went to the movies in 2010
    total_2010 = timothy_2010 + theresa_2010

    # Calculate the total number of movies Timothy and Theresa saw in both 2009 and 2010
    total_movies = total_2009 + total_2010

    result = total_movies
    return result

print(solution())