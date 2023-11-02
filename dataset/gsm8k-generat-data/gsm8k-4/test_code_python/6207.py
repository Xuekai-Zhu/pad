def solution():
    """On a mall-wide sale, Andre bought a $1350 treadmill for a 30% discount and 2 pieces of 45-pound plates for $50 each. How much did Andre pay for the treadmill and plates?"""
    # Calculate the discount on the treadmill
    treadmill_discount = 1350 * 0.3

    # Calculate the price of the treadmill after the discount
    treadmill_price = 1350 - treadmill_discount

    # Calculate the total cost of the two 45-pound plates
    plates_cost = 50 * 2

    # Calculate the total cost of the treadmill and plates
    total_cost = treadmill_price + plates_cost

    result = total_cost
    return result

print(solution())