def solution():
    candies_left = 36
    days = 0

    while candies_left > 0:
        days += 1
        if days % 7 == 1 or days % 7 == 3:
            candies_left -= 2
        else:
            candies_left -= 1

    weeks = days // 7
    result = weeks
    return result

print(solution())