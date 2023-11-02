def solution():
    joy_pencils = 30
    colleen_pencils = 50
    price_per_pencil = 4
    joy_cost = joy_pencils * price_per_pencil
    colleen_cost = colleen_pencils * price_per_pencil
    difference = colleen_cost - joy_cost
    result = difference
    return result

print(solution())