def solution():
    # Number of paintings painted on Day 1
    paintings_day_1 = 2

    # Calculate the total number of paintings painted over 5 days
    total_paintings = paintings_day_1
    for i in range(2, 6):
        daily_paintings = 2**(i-1) * paintings_day_1
        total_paintings += daily_paintings

    result = total_paintings
    return result

print(solution())