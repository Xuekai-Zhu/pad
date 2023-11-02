def solution():
    # Timothy's movie count in 2009
    timothy_2009 = 24

    # Timothy's movie count in 2010
    timothy_2010 = timothy_2009 + 7

    # Theresa's movie count in 2009
    theresa_2009 = timothy_2009 / 2

    # Theresa's movie count in 2010
    theresa_2010 = 2 * timothy_2010

    # Total movies watched by Timothy and Theresa in 2009 and 2010
    total_movies = timothy_2009 + timothy_2010 + theresa_2009 + theresa_2010
    result = total_movies
    return result

print(solution())