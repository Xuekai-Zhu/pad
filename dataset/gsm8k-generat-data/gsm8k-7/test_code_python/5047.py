def solution():
    lucia_day1 = 120
    alina_day1 = lucia_day1 - 20
    
    lucia_day2 = lucia_day1 / 3
    alina_day2 = alina_day1 * 2
    
    total_day3 = alina_day1 + lucia_day1
    
    total_messages = alina_day1 + lucia_day1 + lucia_day2 + alina_day2 + total_day3
    result = total_messages
    return result

print(solution())