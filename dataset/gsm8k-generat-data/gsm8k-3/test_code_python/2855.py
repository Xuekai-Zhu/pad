def solution():
    """For 6 weeks in the summer, Erica treats herself to 1 ice cream cone from the ice cream truck.  Monday, Wednesday and Friday she gets a $2.00 orange creamsicle.  Tuesday and Thursday she gets a $1.50 ice cream sandwich.  Saturday and Sunday she gets a $3.00 Nutty-Buddy.  How much money does she spend on ice cream in 6 weeks?"""
    # Define the prices of each type of ice cream
    ORANGE_PRICE = 2.00
    SANDWICH_PRICE = 1.50
    NUTTY_PRICE = 3.00

    # Define the number of times Erica gets each type of ice cream per week
    orange_per_week = 3
    sandwich_per_week = 2
    nutty_per_week = 2

    # Calculate the total cost of each type of ice cream per week
    orange_cost_per_week = orange_per_week * ORANGE_PRICE
    sandwich_cost_per_week = sandwich_per_week * SANDWICH_PRICE
    nutty_cost_per_week = nutty_per_week * NUTTY_PRICE

    # Calculate the total cost of all the ice cream per week
    total_cost_per_week = orange_cost_per_week + sandwich_cost_per_week + nutty_cost_per_week

    # Calculate the total cost of all the ice cream for 6 weeks
    total_cost = total_cost_per_week * 6

    # Display the total cost
    result = total_cost
    return result

print(solution())