def solution():
    """Oranges have 80 calories and cost $1.20 each. If Timmy has $10 and needs to make sure he gets 400 calories, how much money will he have left after he buys the oranges he needs?"""
    # Define the calorie content and cost of one orange
    ORANGE_CALORIES = 80
    ORANGE_COST = 1.20

    # Define the number of oranges needed to get 400 calories
    oranges_needed = 400 / ORANGE_CALORIES

    # Calculate the total cost of the oranges needed
    total_cost = oranges_needed * ORANGE_COST

    # Calculate the amount of money Timmy will have left
    money_left = 10 - total_cost

    # Display the amount of money Timmy will have left
    result = money_left
    return result

print(solution())