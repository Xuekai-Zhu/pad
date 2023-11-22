def solution():
    
    # Define Mark's initial savings and the cost of the bike
    initial_savings = 50
    bike_cost = 300

    # Define Mark's daily earnings and the number of days Mark has to save
    daily_earnings = 10
    days_to_save = 0

    # Calculate Mark's daily savings
    daily_savings = initial_savings + bike_cost

    # Calculate the number of days Mark has to save
    days_to_save = daily_savings / daily_earnings

    # Display the number of days Mark has to save
    result = days_to_save
    return result

print(solution())