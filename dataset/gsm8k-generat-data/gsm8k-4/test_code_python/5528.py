def solution():
    """40% of a farmer's cattle are males. The rest are females. If a female cow produces 2 gallons of milk a day, how much milk will the farmer get a day if he has 50 male cows?"""
    # Define the total number of cows
    total_cows = 100

    # Calculate the number of female cows
    female_cows = total_cows * 0.6

    # Calculate the number of female cows that produce milk
    milk_cows = female_cows

    # Calculate the total amount of milk produced each day
    milk = milk_cows * 2

    # Add the milk produced by the male cows
    milk += 50 * 0

    # Display the total amount of milk produced each day
    result = milk
    return result

print(solution())