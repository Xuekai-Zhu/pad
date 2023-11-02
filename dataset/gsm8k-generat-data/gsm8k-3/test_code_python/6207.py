def solution():
    """On a mall-wide sale, Andre bought a $1350 treadmill for a 30% discount and 2 pieces of 45-pound plates for $50 each. How much did Andre pay for the treadmill and plates?"""
    # Calculate the discounted price of the treadmill
    treadmill_discount = 0.3
    treadmill_price = 1350
    treadmill_discounted_price = treadmill_price - (treadmill_price * treadmill_discount)

    # Calculate the total cost of the plates
    plate_price = 50
    total_plate_cost = plate_price * 2

    # Calculate the total cost of the treadmill and plates
    total_cost = treadmill_discounted_price + total_plate_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())