def solution():
    # Calculate the total cost for Elle and Andrea
    total_soda_cost = 4 * 1.5  # 4 cans of soda cost $1.50 each
    total_Elle_Andrea_cost = total_soda_cost + 10  # Elle and Andrea are splitting the cost for 4 cans of soda and chicken wings

    # Calculate the total cost for the party
    total_cost = 20 + 2 + total_Elle_Andrea_cost + 5  # Mary buys pasta and bread, Elle and Andrea buy soda and chicken wings, Joe buys a cake

    # Calculate the total cost for everyone except Mary
    total_cost_others = total_Elle_Andrea_cost + 5  # Elle, Andrea and Joe are splitting the cost for soda, chicken wings and cake

    # Calculate how much more Mary spends than the rest of the firm put together
    diff = total_cost - total_cost_others
    result = diff
    return result

print(solution())