def solution():
    """On a mall-wide sale, Andre bought a $1350 treadmill for a 30% discount and 2 pieces of 45-pound plates for $50 each. How much did Andre pay for the treadmill and plates?"""
    treadmill_cost = 1350
    discount_percent = 30
    discount_amount = treadmill_cost * (discount_percent / 100)
    discounted_cost = treadmill_cost - discount_amount
    plate_cost = 50
    num_plates = 2
    total_plate_cost = plate_cost * num_plates
    total_cost = discounted_cost + total_plate_cost
    result = total_cost
    return result

print(solution())