def solution():
    male_percentage = 0.4
    female_percentage = 1 - male_percentage

    male_cows = 0.4 * 100  # Assuming the farmer has 100 cows
    female_cows = 100 - male_cows

    female_milk_production = 2  # gallons per day

    # Calculate the total milk production from all female cows
    total_female_milk_production = female_cows * female_milk_production

    # Calculate the total milk production per day with 50 male cows
    total_milk_production = total_female_milk_production
    result = total_milk_production
    return result

print(solution())