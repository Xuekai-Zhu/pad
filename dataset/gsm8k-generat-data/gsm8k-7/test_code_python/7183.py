def solution():
    fuel_efficiency = 2.5  # 5 miles for every 2 pounds of coal
    remaining_fuel = 160

    # Calculate the total distance that the train can travel before running out of fuel
    total_distance = remaining_fuel * fuel_efficiency
    result = total_distance
    return result

print(solution())