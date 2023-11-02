def solution():
    side_length = 6
    density = 19
    gold_price = 60
    selling_price_factor = 1.5

    # Calculate the volume of the cube
    volume = side_length ** 3

    # Calculate the weight of the gold cube
    weight = volume * density

    # Calculate the cost of buying the gold cube
    cost = weight * gold_price

    # Calculate the selling price of the gold cube
    selling_price = cost * selling_price_factor

    # Calculate the profit from selling the gold cube
    profit = selling_price - cost
    result = profit
    return result

print(solution())