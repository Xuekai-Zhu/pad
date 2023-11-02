def solution():
    """A bond paper ream has 500 sheets and costs $27. An office needs 5000 sheets of bond paper. How much will it cost to buy their needed sheets of paper?"""
    # Define the price and quantity of a single ream of bond paper
    REAM_PRICE = 27
    REAM_QUANTITY = 500

    # Calculate the total cost of buying the needed sheets of paper
    total_cost = (5000 / REAM_QUANTITY) * REAM_PRICE

    # return the result
    result = total_cost
    return result

print(solution())