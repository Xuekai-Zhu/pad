def solution():
    
    total_fuel = 60
    second_third_fuel = total_fuel / 3
    final_third_fuel = second_third_fuel / 2
    first_third_fuel = total_fuel - second_third_fuel - final_third_fuel
    result = first_third_fuel
    return result

print(solution())