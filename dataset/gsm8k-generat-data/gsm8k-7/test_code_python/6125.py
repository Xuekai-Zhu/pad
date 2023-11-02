def solution():
    athlete1_time = 55
    athlete2_time = athlete1_time + 10
    athlete3_time = athlete2_time - 15
    athlete4_time = athlete1_time - 25

    # Calculate the total time for all athletes to finish the relay race
    total_time = athlete1_time + athlete2_time + athlete3_time + athlete4_time
    result = total_time
    return result

print(solution())