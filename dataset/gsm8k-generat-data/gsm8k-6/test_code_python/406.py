def solution():
    # Calculate the total time for the movies and cooking
    movie1_length = 1.5   # hours
    movie2_length = movie1_length + 0.5   # 30 minutes longer than the first movie
    popcorn_time = 10/60   # 10 minutes to make popcorn, converted to hours
    fries_time = 2 * popcorn_time   # twice as long as making popcorn
    total_time = movie1_length + movie2_length + popcorn_time + fries_time   # total time in hours
    result = total_time
    return result

print(solution())