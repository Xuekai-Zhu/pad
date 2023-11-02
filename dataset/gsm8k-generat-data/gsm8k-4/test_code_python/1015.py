def solution():
    """Oranges have 80 calories and cost $1.20 each. If Timmy has $10 and needs to make sure he gets 400 calories, how much money will he have left after he buys the oranges he needs?"""
    # Define the calorie and cost of each orange
    ORANGE_CALORIES = 80
    ORANGE_COST = 1.20

    # Define the amount of money Timmy has and the number of calories he needs
    MONEY = 10
    CALORIES_NEEDED = 400

    # Calculate the number of oranges Timmy needs to buy to get the required calories
    oranges_needed = CALORIES_NEEDED / ORANGE_CALORIES

    # Calculate the cost of the oranges Timmy needs to buy
    cost = oranges_needed * ORANGE_COST

    # Calculate the amount of money Timmy will have left
    remaining_money = MONEY - cost

    result = round(remaining_money, 2)
    return result

print(solution())