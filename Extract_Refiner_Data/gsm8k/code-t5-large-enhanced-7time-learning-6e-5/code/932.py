def solution():
    
    # Define the initial cost of paying for 12-hour and 24-hour stay
    INITIAL_COST = 1000
    INITIAL_HOURS = 12
    INITIAL_DAYS = 24

    # Define the number of pesos added per hour after 12-hour stay
    ADDITIONAL_PER_HOUR = 70

    # Define the number of hours Cameron wants to pay for 24-hour stay
    HOURS_PER_DAY = 24

    # Calculate the number of pesos Cameron would add on the 12-hour mark
    pesos_added_12_hour = ADDITIONAL_PER_HOUR * HOURS_PER_DAY

    # Calculate the number of pesos Cameron would add on the 24-hour mark
    pesos_added_24_hour = ADDITIONAL_PER_HOUR * HOURS_PER_DAY

    # Calculate the total number of pesos Cameron would add on the 12-hour mark
    total_pesos_added_12_hour = pesos_added_12_hour + pesos_added_24_

print(solution())