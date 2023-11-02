def solution():
    # Calculate the volume of the cube
    volume = 6 ** 3

    # Calculate the weight of the gold in the cube
    weight = volume * 19

    # Calculate the cost of the gold
    cost = weight * 60

    # Calculate the selling price of the gold
    selling_price = cost * 1.5

    # Calculate the profit
    profit = selling_price - cost
    result = profit
    return result

print(solution())