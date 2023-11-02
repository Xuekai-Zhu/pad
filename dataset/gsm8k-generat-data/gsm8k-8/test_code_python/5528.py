def solution():
    # Calculate the total number of cattle
    total_cattle = 100 # since 40% are males, 100 - 40 = 60% are females
    # Calculate the number of female cows
    female_cows = total_cattle * 0.6
    # Calculate the total milk produced by female cows
    total_milk = female_cows * 2 # each female cow produces 2 gallons of milk a day
    # Subtract the milk produced by male cows (assume they produce no milk)
    total_milk -= 50 * 0 # since male cows do not produce milk
    result = total_milk
    return result

print(solution())