def solution():
    """Joy has 30 pencils, and Colleen has 50 pencils. If they bought the pencils at $4 each at the store, how much more money did Colleen pay than Joy for her pencils?"""
    joy_pencils = 30
    colleen_pencils = 50
    pencil_price = 4
    joy_cost = joy_pencils * pencil_price
    colleen_cost = colleen_pencils * pencil_price
    difference = colleen_cost - joy_cost
    result = difference
    return result

print(solution())