def solution():
    """Peter is buying a set of glasses. They cost $3 for small glasses and $5 for large ones. He has $50.
    If he buys 8 small ones and leaves with $1 in change, how many large ones did he buy?"""
    # Define the prices of small and large glasses
    small_price = 3
    large_price = 5

    # Define the number of small glasses bought and the amount spent on them
    small_glasses = 8
    small_cost = small_price * small_glasses

    # Calculate the remaining budget after buying small glasses
    remaining_budget = 50 - small_cost + 1

    # Calculate the maximum number of large glasses that can be bought with the remaining budget
    max_large_glasses = remaining_budget // large_price

    # return the result
    result = max_large_glasses
    return result

print(solution())