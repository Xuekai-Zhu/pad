def solution():
    # Define each athlete's running time
    athlete1_time = 55
    athlete2_time = athlete1_time + 10
    athlete3_time = athlete2_time - 15
    athlete4_time = athlete1_time - 25

    # Calculate the total time of the race
    total_time = athlete1_time + athlete2_time + athlete3_time + athlete4_time
    result = total_time
    return result

print(solution())