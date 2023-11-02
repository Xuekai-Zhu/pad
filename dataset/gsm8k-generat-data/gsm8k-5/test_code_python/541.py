def solution():
    younger_sister_cost = 4 * 15  # Tonya spends $15 for each of the 4 dolls for her younger sister. 
    total_spending = 2 * younger_sister_cost  # Tonya plans to spend the same amount on each sister.

    lego_set_cost = 20  # Each lego set costs $20.
    lego_sets = (total_spending - younger_sister_cost) / lego_set_cost  # Subtract younger sister's cost from total spending and divide by cost per lego set.

    result = lego_sets
    return result

print(solution())