def solution():
    total_fish_day1 = 15
    sharks_day1 = total_fish_day1 * 0.25
    total_fish_day2 = total_fish_day1 * 3
    sharks_day2 = total_fish_day2 * 0.25
    total_sharks = sharks_day1 + sharks_day2
    result = total_sharks
    return result

print(solution())