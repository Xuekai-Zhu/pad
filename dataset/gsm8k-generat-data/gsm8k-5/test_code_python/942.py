def solution():
    movie_time = 1.5 * 2  # Paul watches two movies, each of which is 1.5 hours long
    total_time = movie_time * 60  # Convert movie time from hours to minutes
    miles_per_minute = 1 / 12  # Paul can run one mile in 12 minutes, or 1/12 miles per minute

    # Calculate the total distance Paul ran
    distance = total_time * miles_per_minute
    result = distance
    return result

print(solution())