def solution():
    
    days = 5
    breakfast = 1
    lunch = 1
    dinner = 2
    daily_jerky = breakfast + lunch + dinner
    total_jerky_needed = days * daily_jerky
    remaining_jerky = 40 - total_jerky_needed
    jerky_for_brother = remaining_jerky / 2
    remaining_jerky -= jerky_for_brother
    result = remaining_jerky
    return result

print(solution())