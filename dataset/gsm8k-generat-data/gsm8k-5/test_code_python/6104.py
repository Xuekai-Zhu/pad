def solution():
    casey_time = 6 # Casey takes 6 hours to complete the race
    zendaya_time = casey_time * (4/3) # Zendaya takes 1/3 times longer than Casey

    # Calculate the total time both take to complete the race
    total_time = casey_time + zendaya_time

    # Calculate the average time both take to complete the race
    average_time = total_time / 2
    result = average_time
    return result

print(solution())