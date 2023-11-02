def solution():
    # Calculate the number of bracelets sold for $5 each
    sold_for_5 = 60 / 5
    # Calculate the number of bracelets sold for $8
    sold_for_8 = (30 - sold_for_5) / 2
    # Calculate the total revenue
    total_revenue = sold_for_5 * 5 + sold_for_8 * 8
    result = total_revenue
    return result

print(solution())