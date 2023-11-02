def solution():
    # Calculate the total number of pizza doughs that Bruce can make using one sack of flour
    pizzas_per_sack = 15 

    # Calculate the total number of sacks of flour that Bruce uses in a week
    sacks_per_week = 5 * 7  

    # Calculate the total number of pizza doughs that Bruce can make in a week
    total_pizzas = pizzas_per_sack * sacks_per_week
    result = total_pizzas
    return result

print(solution())