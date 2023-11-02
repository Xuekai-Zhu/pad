def solution():
    """In San Diego Zoo, the lion consumes 25 kilograms of meat, and the tiger consumes 20 kilograms of meat per day. If they have 90 kilograms of meat, how many days will the meats last?"""
    # Define the daily consumption of meat
    LION_CONSUMPTION = 25
    TIGER_CONSUMPTION = 20

    # Define the total amount of meat
    TOTAL_MEAT = 90

    # Calculate the total daily consumption of meat
    total_consumption = LION_CONSUMPTION + TIGER_CONSUMPTION

    # Calculate the number of days the meat will last
    days_last = TOTAL_MEAT / total_consumption

    # Display the number of days the meat will last
    result = days_last
    return result

print(solution())