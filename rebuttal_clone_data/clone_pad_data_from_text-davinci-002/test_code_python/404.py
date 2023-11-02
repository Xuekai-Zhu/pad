def solution():
    bales_of_hay = 560
    acres_of_grass = 12
    Monthly_hay = bales_of_hay/5
    horses = 9
    horse_hay = horses * 3
    total_hay = Monthly_hay * 12
    left_over = total_hay - horse_hay
    result = left_over
    return result

print(solution())