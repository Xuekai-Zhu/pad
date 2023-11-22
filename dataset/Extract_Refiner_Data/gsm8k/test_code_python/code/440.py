def solution():
    
    # Convert movie C's length to minutes
    movie_c_length = 1.25 * 60

    # Calculate movie B's length in minutes
    movie_b_length = movie_c_length + 5

    # Calculate movie A's length in minutes
    movie_a_length = movie_b_length / 4

    # Display movie A's length in minutes
    result = movie_a_length
    return result

print(solution())