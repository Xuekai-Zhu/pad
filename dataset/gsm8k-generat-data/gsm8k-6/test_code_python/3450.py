def solution():
    # Calculate the time needed to mow the lawn
    mow_time = 40 * 2  # Carson takes 2 minutes to mow each line

    # Calculate the time needed to plant the flowers
    flower_time = 8 * 7 * 0.5  # Carson takes half a minute to plant each flower

    # Calculate the total time needed for gardening
    total_time = mow_time + flower_time
    result = total_time
    return result

print(solution())