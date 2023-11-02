def solution():
    """John used to buy 4 coffees a day for $2 each. They raised the price by 50% so he cut the number of coffees he drinks in half. How much money does he save per day compared to what he used to spend?"""
    # Define the initial cost and the reduction in the number of coffees
    initial_cost = 4 * 2
    reduced_coffees = 4 / 2

    # Calculate the new price per coffee after the 50% increase
    new_price = 2 * 1.5

    # Calculate the new daily cost
    new_cost = reduced_coffees * new_price

    # Calculate the savings per day
    savings = initial_cost - new_cost

    # return the result
    result = savings
    return result

print(solution())