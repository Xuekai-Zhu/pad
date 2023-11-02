def solution():
    """Tony has $87. He needs to buy some cheese, which costs $7 a pound and a pound of beef that costs $5 a pound. After buying the beef and his cheese, he has $61 left. How many pounds of cheese did he buy?"""
    # Define the cost of cheese and beef per pound
    CHEESE_PRICE = 7
    BEEF_PRICE = 5

    # Define the initial amount of money Tony has and the amount left after buying the beef and cheese
    initial_money = 87
    remaining_money = 61

    # Calculate the cost of the beef
    beef_cost = BEEF_PRICE * 1  # Tony buys 1 pound of beef

    # Calculate the cost of the cheese and the number of pounds of cheese Tony can buy
    cheese_cost = initial_money - remaining_money - beef_cost
    cheese_pounds = cheese_cost / CHEESE_PRICE

    # Display the number of pounds of cheese Tony bought
    result = cheese_pounds
    return result

print(solution())