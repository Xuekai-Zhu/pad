def solution():
    
    total_birds = 50
    day1_birds = 50
    day2_birds = 120
    day3_birds = 0
    day4_birds = 120
    day5_birds = 120
    day6_birds = 20
    day7_birds = 90
    total_day1_birds = day1_birds + day2_birds + day3_birds + day4_birds + day6_birds + day7_birds
    average_birds_per_day = total_birds / 7
    result = average_birds_per_day
    return result

print(solution())