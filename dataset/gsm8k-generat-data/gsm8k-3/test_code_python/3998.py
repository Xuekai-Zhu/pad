def solution():
    """Tim decides to get animals for his zoo.  He buys 3 goats for $400 each.  He gets twice as many llamas which cost 50% more each.  How much did he spend?"""
    # Define the price of a goat and the increase percentage for llamas
    goat_price = 400
    llama_price_increase = 0.5

    # Calculate the cost of the goats
    goat_cost = 3 * goat_price

    # Calculate the price of a llama
    llama_price = goat_price * (1 + llama_price_increase)

    # Calculate the cost of the llamas
    llama_cost = 2 * llama_price * goat_price

    # Calculate the total cost
    total_cost = goat_cost + llama_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())