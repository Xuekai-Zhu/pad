def solution():
    num_washes = 20  # Jim bought a package of 20 car washes
    discount = 0.6  # Jim gets a 40% discount for buying a package
    regular_price = 15  # A car wash normally costs $15

    # Calculate the discounted price per car wash
    discounted_price = regular_price * discount

    # Calculate the total cost of the package
    total_cost = num_washes * discounted_price
    result = total_cost
    return result

print(solution())