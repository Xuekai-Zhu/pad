def solution():
    # Calculate the amount of lawn mowed with the riding mower
    riding_mower_lawn = 0.75 * 8

    # Calculate the amount of lawn mowed with the push mower
    push_mower_lawn = 8 - riding_mower_lawn

    # Calculate the time taken to mow with the riding mower
    riding_mower_time = riding_mower_lawn / 2

    # Calculate the time taken to mow with the push mower
    push_mower_time = push_mower_lawn / 1

    # Calculate the total time taken to mow the lawn
    total_time = riding_mower_time + push_mower_time
    result = total_time
    return result

print(solution())