def solution():
    permit_cost = 250  # Permit cost is fixed at $250
    contractor_cost = 150 * 3 * 5  # Contractor works for 3 days, 5 hours per day, and charges $150 per hour
    inspector_discount = 0.8  # Inspector gives an 80% discount on the usual price
    inspector_cost = (150 * 3) * (1 - inspector_discount)  # Inspector works for 3 hours, charges $150 per hour, and gives an 80% discount

    # Calculate the total cost by adding all the expenses
    total_cost = permit_cost + contractor_cost + inspector_cost
    result = total_cost
    return result

print(solution())