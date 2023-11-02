def solution():
    
    paintings_per_day = [2]
    for i in range(1, 5):
        paintings = paintings_per_day[i-1]*2
        paintings_per_day.append(paintings)
    total_paintings = sum(paintings_per_day)
    result = total_paintings
    return result

print(solution())