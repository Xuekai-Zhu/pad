def solution():
    """Peter is buying a set of glasses. They cost $3 for small glasses and $5 for large ones. He has $50. If he buys 8 small ones and leaves with $1 in change, how many large ones did he buy?"""
    # Define the cost of each type of glass
    SMALL_GLASS_PRICE = 3
    LARGE_GLASS_PRICE = 5

    # Define the number of small glasses that Peter buys
    num_small_glasses = 8

    # Define the total amount that Peter has to spend
    total_spending = 50

    # Calculate the cost of the small glasses Peter buys
    small_glass_cost = num_small_glasses * SMALL_GLASS_PRICE

    # Calculate the amount of money Peter has left after buying the small glasses
    money_left = total_spending - small_glass_cost

    # Calculate the maximum number of large glasses Peter can buy with the money left
    max_num_large_glasses = money_left // LARGE_GLASS_PRICE

    # Calculate the actual number of large glasses Peter buys (including the change)
    num_large_glasses = (money_left - 1) // LARGE_GLASS_PRICE

    # Display the number of large glasses Peter buys
    result = num_large_glasses
    return result

print(solution())