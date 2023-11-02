def solution():
    """Tracy set up a booth at an art fair. 20 people came to look at her art. Four of those customers bought two paintings each. The next 12 of those customers bought one painting each. The last 4 customers bought four paintings each. How many paintings did Tracy sell at the art fair?"""
    # Calculate the number of paintings sold to customers who bought 2 each
    paintings_double_buyers = 4 * 2

    # Calculate the number of paintings sold to customers who bought 1 each
    paintings_single_buyers = 12 * 1

    # Calculate the number of paintings sold to customers who bought 4 each
    paintings_quad_buyers = 4 * 4

    # Calculate the total number of paintings sold
    total_paintings = paintings_double_buyers + paintings_single_buyers + paintings_quad_buyers

    # return the result
    result = total_paintings
    return result

print(solution())