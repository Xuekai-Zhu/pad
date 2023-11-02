def solution():
    """Movie A was one-fourth the length of Movie B. Movie B was 5 minutes longer than Movie C. Movie C was 1.25 hours. How many minutes long was Movie A?"""
    movie_c_length = 1.25*60 # in minutes
    movie_b_length = movie_c_length + 5
    movie_a_length = movie_b_length / 4
    
    return movie_a_length

print(solution())