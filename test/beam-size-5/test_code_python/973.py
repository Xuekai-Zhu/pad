def solution():
    
    # Define the amount of sunscreen per bottle
    SUNSCREEN_PER_BOTTLE = 8

    # Define the number of hours Pamela will be outside per day
    HOURS_PER_DAY = 4

    # Define the number of days Pamela will be outside
    days = 8

    # Calculate the total amount of sunscreen Pamela will need to pack
    total_sunscreen = SUNSCREEN_PER_BOTTLE * HOURS_PER_DAY * days

    # Display the total amount of sunscreen Pamela needs to pack
    result = total_sunscreen
    return result

print(solution())