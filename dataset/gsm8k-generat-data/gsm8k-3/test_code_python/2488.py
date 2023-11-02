def solution():
    """Timothy and Theresa go to the movies very often. Timothy went to the movies 7 more times in 2010 that he did in 2009. In 2009, Timothy went to the movies 24 times. In 2010 Theresa went to see twice as many movies as Timothy did, but in 2009, she only saw half as many as he did. How many movies did Timothy and Theresa go on in both 2009 and 2010?"""
    # Timothy's number of movie visits in 2009
    timothy_2009 = 24

    # Theresa's number of movie visits in 2009
    theresa_2009 = timothy_2009 / 2

    # Timothy's number of movie visits in 2010
    timothy_2010 = timothy_2009 + 7

    # Theresa's number of movie visits in 2010
    theresa_2010 = timothy_2010 * 2

    # Total number of movie visits by Timothy and Theresa in both years
    total_visits = timothy_2009 + theresa_2009 + timothy_2010 + theresa_2010

    # Display the total number of movie visits
    result = total_visits
    return result

print(solution())