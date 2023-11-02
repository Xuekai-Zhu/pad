def solution():
    """Five people are planning a party. Sonja will buy a loaf of French bread ($3 a loaf) and a platter of cold cuts ($23). Barbara will buy the soda ($1 per person) and two boxes of crackers ($2 per box). Mario and Rick will split the cost of two packages of Cheese Doodles ($3 per package). Danica will supply a package of paper plates for $4. How much more will Sonja spend than the rest of the office put together?"""
    # Calculate the total cost of Sonja's purchases
    sonja_cost = 3 + 23

    # Calculate the total cost of Barbara's purchases
    num_people = 5
    soda_cost = num_people * 1
    crackers_cost = 2 * 2
    barbara_cost = soda_cost + crackers_cost

    # Calculate the total cost of Mario and Rick's purchases
    doodles_cost = 2 * 3 / 2
    mario_rick_cost = doodles_cost

    # Calculate the total cost of Danica's purchases
    danica_cost = 4

    # Calculate the total cost of all purchases except Sonja's
    other_cost = barbara_cost + mario_rick_cost + danica_cost

    # Calculate how much more Sonja spent than the rest of the office put together
    difference = sonja_cost - other_cost

    # Display the difference
    result = difference
    return result

print(solution())