def solution():
    num_drinks = 2  # Wade buys 2 drinks
    drink_cost = 4  # Each drink costs $4
    total_cost = 26  # Wade spends a total of $26
    sandwich_cost = (total_cost - (num_drinks * drink_cost)) / 3  # Wade buys 3 sandwiches

    result = sandwich_cost
    return result

print(solution())