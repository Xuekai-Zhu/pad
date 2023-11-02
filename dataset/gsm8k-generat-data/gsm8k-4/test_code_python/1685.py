def solution():
    """Clinton buys a burger meal for lunch for $6.00 and up sizes his fries and drinks for $1.00 more. If Clinton buys this same meal every day for 5 days, how much does he spend on lunch?"""
    # Define the cost of the burger meal and the cost of up-sizing
    BURGER_MEAL_COST = 6.00
    UP_SIZE_COST = 1.00

    # Calculate the cost of the meal with up-sized fries and drinks
    meal_cost = BURGER_MEAL_COST + UP_SIZE_COST

    # Calculate the total cost of lunch for 5 days
    total_cost = meal_cost * 5

    # return the result
    result = total_cost
    return result

print(solution())