def solution():
    """40% of a farmer's cattle are males. The rest are females. If a female cow produces 2 gallons of milk a day, how much milk will the farmer get a day if he has 50 male cows?"""
    # Define the percentage of cattle that are females
    FEMALE_PERCENTAGE = 60

    # Define the milk production per female cow per day
    FEMALE_MILK_PRODUCTION = 2

    # Define the number of male cows
    male_cows = 50

    # Calculate the number of female cows
    total_cows = 100 # assuming there are 100 cows in total
    female_cows = total_cows - male_cows

    # Calculate the total milk production per day
    total_milk_production = female_cows * FEMALE_MILK_PRODUCTION

    # Display the total milk production per day
    result = total_milk_production
    return result

print(solution())