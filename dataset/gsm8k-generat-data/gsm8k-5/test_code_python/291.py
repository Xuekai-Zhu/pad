def solution():
    fuel_last_week = 15 / (1-0.2)  # Mary used 20% less fuel last week, so this is equal to 15 divided by 0.8
    total_fuel = fuel_last_week + 15  # Mary used 15 gallons of fuel this week, so the total fuel used is the sum of the two weeks
    result = total_fuel
    return result

print(solution())