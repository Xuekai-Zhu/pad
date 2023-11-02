def solution():
    cakes = 2  # Claire wants to make 2 cakes
    flour_per_cake = 2  # Two packages of flour are required for making a cake
    price_per_package = 3  # Each package of flour costs $3

    # Calculate the total cost of flour for 2 cakes
    total_flour_cost = cakes * flour_per_cake * price_per_package
    result = total_flour_cost
    return result

print(solution())