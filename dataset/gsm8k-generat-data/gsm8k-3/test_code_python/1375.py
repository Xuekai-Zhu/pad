def solution():
    """A farmer owns a hog that recently gave birth to 6 piglets.  If the farmer raises the piglets until they are fully grown, he can sell the fully grown pig for $300.  Each piglet must grow for at least 12 months before it is large enough to be sold. It costs the farmer $10 per month to feed each animal until it is sold.  If the farmer sells 3 pigs after 12 months, and the remaining 3 pigs after 16 months, how much profit did he earn in total (after deducting the cost of food)?"""
    # Define the price of a fully grown pig
    PIG_PRICE = 300

    # Define the cost of feeding each animal per month
    FEEDING_COST = 10

    # Define the time in months for each group of piglets to grow
    GROW_TIME_1 = 12
    GROW_TIME_2 = 16

    # Define the number of piglets in each group
    PIGLETS_1 = 3
    PIGLETS_2 = 3

    # Calculate the cost of feeding each piglet before it is sold
    feeding_cost_1 = GROW_TIME_1 * FEEDING_COST
    feeding_cost_2 = GROW_TIME_2 * FEEDING_COST

    # Calculate the total cost of feeding all the piglets
    total_feeding_cost = feeding_cost_1 * PIGLETS_1 + feeding_cost_2 * PIGLETS_2

    # Calculate the total profit from selling the fully grown pigs
    total_profit = PIG_PRICE * (PIGLETS_1 + PIGLETS_2) - total_feeding_cost

    # Display the total profit
    result = total_profit
    return result

print(solution())