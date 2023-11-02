def solution():
    # Calculate the volume and weight of the gold cube
    volume = 6**3  # the cube is 6 cm on each side
    weight = volume * 19  # the density of gold is 19 grams per cubic centimeter

    # Calculate the cost and the selling price
    cost = weight * 60  # he buys the gold for $60 per gram
    selling_price = cost * 1.5  # he sells it for 1.5 times its gold value

    # Calculate the profit
    profit = selling_price - cost
    result = profit
    return result

print(solution())