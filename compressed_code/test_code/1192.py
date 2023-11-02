def solution():
    
    num_days = 5
    paintings = 2
    total_paintings = 2
    for i in range(1, num_days):
        paintings *= 2
        total_paintings += paintings

    result = total_paintings
    return result

print(solution())