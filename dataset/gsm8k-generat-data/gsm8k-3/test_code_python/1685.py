def solution():
    """Clinton buys a burger meal for lunch for $6.00 and up sizes his fries and drinks for $1.00 more. If Clinton buys this same meal every day for 5 days, how much does he spend on lunch?"""
    # Define the cost of the burger meal and up-sized fries and drinks
    BURGER_MEAL_COST = 6.00
    UP_SIZE_COST = 1.00

    # Calculate the total cost of lunch for 5 days
    total_cost = (BURGER_MEAL_COST + UP_SIZE_COST) * 5

    # Display the total cost
    result = total_cost
    return result

print(solution())