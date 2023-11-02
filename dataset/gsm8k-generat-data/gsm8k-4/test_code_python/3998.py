def solution():
    """Tim decides to get animals for his zoo. He buys 3 goats for $400 each. He gets twice as many llamas which cost 50% more each. How much did he spend?"""
    # Define the cost of the goats and the number of goats purchased
    goat_cost = 400
    num_goats = 3

    # Calculate the total cost of the goats
    total_goat_cost = goat_cost * num_goats

    # Define the cost of one llama and calculate the cost of one llama after a 50% increase in price
    llama_cost = goat_cost * 1.5

    # Calculate the number of llamas purchased
    num_llamas = num_goats * 2

    # Calculate the total cost of the llamas
    total_llama_cost = llama_cost * num_llamas

    # Calculate the total cost of all animals
    total_cost = total_goat_cost + total_llama_cost

    # Return the total cost
    return total_cost

print(solution())