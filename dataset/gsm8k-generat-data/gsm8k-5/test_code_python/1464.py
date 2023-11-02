def solution():
    daily_production = 7000  # The company was producing 7000 toilet papers per day before the outbreak
    increased_production = daily_production * 3  # The company had to ramp up its production three times more
    days_in_march = 31  # March has 31 days

    # Calculate the total toilet paper production in March 2020
    total_production = increased_production * days_in_march
    result = total_production
    return result

print(solution())