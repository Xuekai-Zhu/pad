def solution():
    """Five people are planning a party. Sonja will buy a loaf of French bread ($3 a loaf) and a platter of cold cuts ($23). Barbara will buy the soda ($1 per person) and two boxes of crackers ($2 per box). Mario and Rick will split the cost of two packages of Cheese Doodles ($3 per package). Danica will supply a package of paper plates for $4. How much more will Sonja spend than the rest of the office put together?"""
    sonja_total = 3 + 23
    barbara_total = 5 + 4
    mario_rick_total = 3 * 2 / 2
    office_total = sonja_total + barbara_total + mario_rick_total
    sonja_difference = sonja_total - office_total
    result = sonja_difference
    return result

print(solution())