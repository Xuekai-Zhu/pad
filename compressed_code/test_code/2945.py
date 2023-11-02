def solution():
    
    day1_fish = 15
    day2_fish = 3 * day1_fish
    total_fish = day1_fish + day2_fish
    shark_percentage = 0.25
    shark_count = total_fish * shark_percentage
    result = shark_count
    return result

print(solution())