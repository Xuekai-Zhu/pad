def solution():
    """Tony has $87. He needs to buy some cheese, which costs $7 a pound and a pound of beef that costs $5 a pound. After buying the beef and his cheese, he has $61 left. How many pounds of cheese did he buy?"""
    # Define the cost of beef and cheese per pound
    BEEF_COST = 5
    CHEESE_COST = 7

    # Define the initial amount of money Tony has
    initial_money = 87

    # Define the amount of money Tony has left after buying the beef and cheese
    remaining_money = 61

    # Define the number of pounds of beef Tony bought
    beef_pounds = 1

    # Calculate the cost of the beef
    beef_cost = beef_pounds * BEEF_COST

    # Calculate the amount of money Tony spent on cheese
    cheese_cost = initial_money - remaining_money - beef_cost

    # Calculate the number of pounds of cheese Tony bought
    cheese_pounds = cheese_cost / CHEESE_COST

    result = round(cheese_pounds)
    return result

print(solution())