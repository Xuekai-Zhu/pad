def solution():
    """A company bought $400000 worth of equipment from a retailer business, but pieces of equipment worth 40% of the total number were faulty. If they returned the faulty pieces of equipment to the seller, calculate the total amount of money spent on functioning pieces of equipment."""
    equipment_cost = 400000
    faulty_percent = 40
    functioning_percent = 100 - faulty_percent
    functioning_cost = functioning_percent/100 * equipment_cost
    result = functioning_cost
    return result

print(solution())