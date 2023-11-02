def solution():
    # Define Casey's marathon time
    casey_time = 6

    # Calculate Zendaya's marathon time
    zendaya_time = casey_time * (1 + 1/3)

    # Calculate the average time for the two
    average_time = (casey_time + zendaya_time) / 2
    result = average_time
    return result

print(solution())