def solution():
    """Lightning McQueen, the race car, cost 140000$. Mater only cost 10 percent of that, and Sally McQueen cost triple what Mater costs. How much does Sally McQueen cost?"""
    # Define the cost of Lightning McQueen
    lightning_cost = 140000

    # Calculate the cost of Mater
    mater_cost = lightning_cost * 0.1

    # Calculate the cost of Sally McQueen
    sally_cost = mater_cost * 3

    # return the result
    result = sally_cost
    return result

print(solution())