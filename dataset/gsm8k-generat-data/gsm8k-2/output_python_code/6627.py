def solution():
    """Tracy set up a booth at an art fair. 20 people came to look at her art. Four of those customers bought two paintings each. The next 12 of those customers bought one painting each. The last 4 customers bought four paintings each. How many paintings did Tracy sell at the art fair?"""
    double_buyers = 4 * 2
    single_buyers = 12 * 1
    quadruple_buyers = 4 * 4
    total_paintings_sold = double_buyers + single_buyers + quadruple_buyers
    result = total_paintings_sold
    return result

print(solution())