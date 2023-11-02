def solution():
    """Tim decides to get animals for his zoo. He buys 3 goats for $400 each. He gets twice as many llamas which cost 50% more each. How much did he spend?"""
    goat_price = 400
    num_goats = 3
    llama_price = 1.5 * goat_price
    num_llamas = 2 * num_goats
    total_cost = (goat_price * num_goats) + (llama_price * num_llamas)
    result = total_cost
    return result

print(solution())