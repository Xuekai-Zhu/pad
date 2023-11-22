def solution():
    
    # Define the amount of meat sold per hour and the number of hours worked per day
    MEAT_PER_HOUR = 15
    HOURS_PER_DAY = 10

    # Define the weight of the bull
    BULL_WEIGHT = 750

    # Calculate the total amount of meat sold per day
    total_meat_per_day = MEAT_PER_HOUR * HOURS_PER_DAY

    # Calculate the number of days it will take to sell the meat from Bill's bull
    days_to_sell_meat = BULL_WEIGHT / total_meat_per_day

    # Display the number of days
    result = days_to_sell_meat
    return result

print(solution())