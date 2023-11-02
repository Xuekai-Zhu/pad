def solution():
    # Calculate the total cost of treats
    cost_Reeses = 4 * 9 # cost of 4 bags of Reese's at $9 per bag
    cost_Snickers = 3 * 5 # cost of 3 bags of Snickers at $5 per bag
    cost_Skittles = 5 * 7 # cost of 5 bags of Skittles at $7 per bag
    total_cost_treats = cost_Reeses + cost_Snickers + cost_Skittles

    # Calculate the total cost of the unicorn piñata and treats
    total_cost = total_cost_treats + 13 # $13 for the unicorn piñata
    result = total_cost
    return result

print(solution())