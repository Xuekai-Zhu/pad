def solution():
    # Calculate the number of shirts made in the first hour
    first_hour_rate = 1/12 # shirts per minute
    first_hour = 60 * first_hour_rate # shirts per hour

    # Calculate the number of shirts made in the second hour
    second_hour_rate = 1/6 # shirts per minute
    second_hour = 60 * second_hour_rate # shirts per hour

    # Calculate the total number of shirts made
    total_shirts = first_hour + second_hour
    result = total_shirts
    return result

print(solution())