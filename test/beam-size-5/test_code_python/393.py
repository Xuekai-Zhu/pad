def solution():
    
    # Define the initial amount in Mark's bank account and the daily earnings
    initial_amount = 50
    daily_earnings = 10

    # Define the cost of the bike
    bike_cost = 300

    # Calculate the amount Mark needs to save
    amount_to_save = bike_cost - initial_amount

    # Calculate the number of days Mark needs to save
    days_to_save = amount_to_save / daily_earnings

    # Display the number of days Mark needs to save
    result = days_to_save
    return result

print(solution())