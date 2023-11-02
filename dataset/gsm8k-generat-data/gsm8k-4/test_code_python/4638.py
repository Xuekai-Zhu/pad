def solution():
    """Five people are planning a party. Sonja will buy a loaf of French bread ($3 a loaf) and a platter of cold cuts ($23). Barbara will buy the soda ($1 per person) and two boxes of crackers ($2 per box). Mario and Rick will split the cost of two packages of Cheese Doodles ($3 per package). Danica will supply a package of paper plates for $4. How much more will Sonja spend than the rest of the office put together?"""
    # Calculate the total cost of Barbara's purchases
    num_people = 5
    soda_price = 1
    crackers_price = 2
    soda_cost = num_people * soda_price
    crackers_cost = 2 * crackers_price
    barbara_cost = soda_cost + crackers_cost

    # Calculate the total cost of Mario and Rick's purchases
    num_packages = 2
    price_per_package = 3
    mario_rick_cost = (num_packages * price_per_package) / 2

    # Calculate the total cost of Danica's purchase
    danica_cost = 4

    # Calculate the total cost of Sonja's purchases
    french_bread_price = 3
    cold_cuts_price = 23
    sonja_cost = french_bread_price + cold_cuts_price

    # Calculate the total cost of everyone else's purchases
    others_cost = barbara_cost + mario_rick_cost + danica_cost

    # Calculate the difference between Sonja's cost and everyone else's cost
    difference = sonja_cost - others_cost

    result = difference
    return result

print(solution())