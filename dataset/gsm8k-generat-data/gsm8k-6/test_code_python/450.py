def solution():
    # Calculate the total number of gallons of milk Flora needs to drink in 3 weeks
    total_gallons = 105 

    # Calculate the average number of gallons Flora needs to drink per day
    average_daily_gallons = total_gallons / (3*7)  # 3 weeks = 21 days

    # Calculate the extra gallons Flora needs to drink daily
    extra_gallons_daily = average_daily_gallons - 3  

    result = extra_gallons_daily
    return result

print(solution())