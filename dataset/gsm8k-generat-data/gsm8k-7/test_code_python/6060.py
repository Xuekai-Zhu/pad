def solution():
    joy_pencils = 30
    colleen_pencils = 50
    price_per_pencil = 4

    # Calculate the total cost of Joy's pencils
    joy_cost = joy_pencils * price_per_pencil

    # Calculate the total cost of Colleen's pencils
    colleen_cost = colleen_pencils * price_per_pencil

    # Calculate the difference in cost between Colleen and Joy's pencils
    difference = colleen_cost - joy_cost
    result = difference
    return result

print(solution())