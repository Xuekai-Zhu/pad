def solution():
    fuel_cost = 3  # The cost of diesel fuel is $3 per gallon
    weekly_fuel_cost = 36  # Mr. Alvarez spends $36 on diesel fuel each week
    gallons_per_week = weekly_fuel_cost / fuel_cost  # Calculate the amount of fuel used in one week
    total_gallons = gallons_per_week * 2  # Mr. Alvarez wants to know the amount of fuel used in two weeks
    result = total_gallons
    return result

print(solution())