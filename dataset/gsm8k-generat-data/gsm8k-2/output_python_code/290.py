def solution():
    """Mary used 15 gallons of fuel this week. Last week she used 20% less. How much fuel did she use in total for the two weeks?"""
    this_week_fuel = 15
    last_week_fuel = this_week_fuel / 0.8
    total_fuel = this_week_fuel + last_week_fuel
    result = total_fuel
    return result

print(solution())