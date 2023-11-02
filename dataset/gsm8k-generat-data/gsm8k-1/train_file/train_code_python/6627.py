def solution():
    """Tracy set up a booth at an art fair. 20 people came to look at her art. Four of those customers bought two paintings each. The next 12 of those customers bought one painting each. The last 4 customers bought four paintings each. How many paintings did Tracy sell at the art fair?"""
    customers = 20
    total_paintings = 0
    paintings_bought_by_4 = 4 * 4
    paintings_bought_by_12 = 12 * 1
    paintings_bought_by_4_individuals = 4 * 2
    total_paintings += paintings_bought_by_4 + paintings_bought_by_12 + paintings_bought_by_4_individuals
    result = total_paintings
    return result

print(solution())