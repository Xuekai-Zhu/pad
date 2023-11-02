def solution():
    former_rent_cost = 2 * 750  # $2 per sq ft for a 750 sq ft apartment
    new_rent_cost = 2800 / 2  # splitting costs evenly with roommate
    savings_per_month = former_rent_cost - new_rent_cost
    total_savings_per_year = savings_per_month * 12
    result = total_savings_per_year
    return result

print(solution())