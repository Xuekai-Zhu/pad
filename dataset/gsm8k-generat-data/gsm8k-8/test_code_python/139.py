def solution():
    # Define the number of times Janice goes up and down the stairs
    up_times = 5
    down_times = 3

    # Calculate the total flights of stairs Janice walks up and down in a single day
    total_stairs = (up_times + down_times) * 3
    result = total_stairs
    return result

print(solution())