def solution():
    """Chenny bought 9 plates at $2 each. She also bought spoons at $1.50 each. How many spoons did Chenny buy if she paid a total of $24 for the plates and spoon?"""
    plates_cost = 9 * 2
    total_cost = 24
    spoons_cost = total_cost - plates_cost
    spoons_bought = spoons_cost / 1.5
    result = spoons_bought
    return result

print(solution())