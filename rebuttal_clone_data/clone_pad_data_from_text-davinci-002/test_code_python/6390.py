def solution():
    horses = 3
    water_needed_per_horse = 5 + 2
    days = 28
    total_horses = horses + 5
    total_water_needed = total_horses * water_needed_per_horse * days
    result = total_water_needed
    return result

print(solution())