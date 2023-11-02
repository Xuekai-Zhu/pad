def solution():
    total_time = 8 * 60  # Total time in minutes

    # Calculate the time Lilly spent cleaning
    lilly_time = total_time / 4

    # Calculate the time Fiona spent cleaning
    fiona_time = total_time - lilly_time

    result = fiona_time
    return result

print(solution())