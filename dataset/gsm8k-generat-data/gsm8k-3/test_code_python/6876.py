def solution():
    """Selena got a tip today that amounted to $99. She pampered herself by eating at a 5-star hotel. She indulged herself with 2 steak meals that cost $24 each plate. She also ordered 2 types of burgers which cost $3.5 each, and 3 cups of ice cream which cost $2 each. How much money will Selena be left with?"""
    # Define the cost of each item
    STEAK_COST = 24
    BURGER_COST = 3.5
    ICE_CREAM_COST = 2

    # Calculate the total cost of the meal
    total_cost = 2*STEAK_COST + 2*BURGER_COST + 3*ICE_CREAM_COST

    # Calculate the amount left after paying for the meal
    amount_left = 99 - total_cost

    # Display the amount left
    result = amount_left
    return result

print(solution())