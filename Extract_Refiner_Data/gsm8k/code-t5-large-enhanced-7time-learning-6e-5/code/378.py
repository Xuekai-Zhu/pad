def solution():
    
    # Define the initial number of silver and gold pesos
    initial_silver = 50
    initial_gold = 80

    # Calculate the number of silver and gold pesos Anna has
    anna_silver = initial_silver * 2
    anna_gold = initial_gold + 40

    # Calculate the total number of pesos they have together
    total_pesos = initial_silver + initial_gold + anna_silver + anna_gold

    # return the result
    result = total_pesos
    return result

print(solution())