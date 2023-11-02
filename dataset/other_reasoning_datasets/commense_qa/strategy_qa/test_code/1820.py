def solution():
    # Define the relevant information
    popeye_uses_spinach = True
    movie_is_about_popeye = True
    popeye_consumes_spinach_in_movie = True
    
    # Check if spinach has been a source of power in a comic movie
    if popeye_uses_spinach and movie_is_about_popeye and popeye_consumes_spinach_in_movie:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())