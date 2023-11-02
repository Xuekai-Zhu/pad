def solution():
     first_two_tanks = 8 * 2
     other_two_tanks = (8 - 2) * 2
     total_water = first_two_tanks + other_two_tanks
     gallons_per_week = total_water / 4
     result = gallons_per_week
     return result

print(solution())