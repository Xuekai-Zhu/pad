def solution():
    # Calculate total miles driven in a week
    weekly_miles = (50 * 3) + (100 * 4)

    # Calculate total miles driven in a year
    yearly_miles = weekly_miles * 52

    # Calculate total cost of mileage
    mileage_cost = yearly_miles * 0.1

    # Calculate total cost of weekly fee
    weekly_fee = 100 * 52

    # Calculate total cost for the year
    total_cost = mileage_cost + weekly_fee
    result = total_cost
    return result

print(solution())