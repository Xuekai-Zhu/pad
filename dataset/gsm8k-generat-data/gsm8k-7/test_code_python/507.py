def solution():
    price_per_pound = 15
    num_pounds = 20

    # Calculate the total amount of steak that James gets, with the BOGO deal
    total_steak = num_pounds * 2

    # Calculate the total cost of all the steak that James buys
    total_cost = total_steak * price_per_pound
    result = total_cost
    return result

print(solution())