def solution():
    """Selena got a tip today that amounted to $99. She pampered herself by eating at a 5-star hotel. She indulged herself with 2 steak meals that cost $24 each plate. She also ordered 2 types of burgers which cost $3.5 each, and 3 cups of ice cream which cost $2 each. How much money will Selena be left with?"""
    # Define the cost of Selena's meal
    meal_cost = 2 * 24 + 2 * 3.5 + 3 * 2

    # Calculate the total cost of the meal, including the tip
    total_cost = meal_cost + 99

    # Calculate the money Selena will be left with after paying for her meal
    left_money = 0 if total_cost < 0 else total_cost

    result = left_money
    return result

print(solution())