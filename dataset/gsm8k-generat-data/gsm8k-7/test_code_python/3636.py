def solution():
    savings = 2225
    rent_per_month = 1250
    months_advance = 2
    deposit = 500

    # Calculate the total cost of renting the apartment
    total_rent_cost = (rent_per_month * months_advance) + deposit

    # Calculate the difference between the total cost and her savings
    difference = total_rent_cost - savings
    result = difference
    return result

print(solution())