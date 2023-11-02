def solution():
    
    sandwiches = 12
    eaten_first_day = sandwiches // 2
    eaten_second_day = eaten_first_day - 2
    remaining_sandwiches = sandwiches - eaten_first_day - eaten_second_day
    result = remaining_sandwiches
    return result

print(solution())