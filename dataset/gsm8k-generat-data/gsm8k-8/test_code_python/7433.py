def solution():
    # Define the cost of the games console and Woody's current savings
    console_cost = 282
    current_savings = 42

    # Calculate the amount of money Woody needs to save
    money_to_save = console_cost - current_savings

    # Calculate the number of weeks it will take to save the necessary money
    weeks_to_save = money_to_save / 24
    result = weeks_to_save
    return result

print(solution())