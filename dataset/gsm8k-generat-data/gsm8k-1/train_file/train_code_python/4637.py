def solution():
    """Five people are planning a party. Sonja will buy a loaf of French bread ($3 a loaf) and a platter of cold cuts ($23). Barbara will buy the soda ($1 per person) and two boxes of crackers ($2 per box). Mario and Rick will split the cost of two packages of Cheese Doodles ($3 per package). Danica will supply a package of paper plates for $4. How much more will Sonja spend than the rest of the office put together?"""
    sonja_cost = 3 + 23
    barbara_cost = 1 * 5 + 2 * 2
    mario_rick_cost = 3 * 2 / 2
    danica_cost = 4
    total_cost = sonja_cost + barbara_cost + mario_rick_cost + danica_cost
    rest_cost = total_cost - sonja_cost
    difference = sonja_cost - rest_cost
    result = difference
    return result

print(solution())