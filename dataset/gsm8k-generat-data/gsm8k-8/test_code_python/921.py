def solution():
    # Define the number of guests who drank each beverage
    soda_drinkers = 90/2
    water_drinkers = 90/3
    juice_consumers = 90*4/5

    # Calculate the total number of cans and bottles used
    total_cans_bottles = 50 + 50 + 50

    # Calculate the number of recyclable cans and bottles
    recyclable = total_cans_bottles - (soda_drinkers + water_drinkers + juice_consumers)

    result = recyclable
    return result

print(solution())