def solution():
     fuel = 60
     fuel_per_third = fuel / 3
     fuel_for_second_third = fuel_per_third * 2
     fuel_for_final_third = fuel_for_second_third / 2
     fuel_for_first_third = fuel - (fuel_for_second_third + fuel_for_final_third)
     result = fuel_for_first_third
     return result

print(solution())