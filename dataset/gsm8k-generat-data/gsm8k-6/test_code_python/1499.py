def solution():
    # Calculate the amount of money made from the family's purchase
    family_purchase = (4 * 5) + (3 * 2)  # 4 hard shell tacos cost $5 each, and 3 soft tacos cost $2 each

    # Calculate the total number of soft tacos sold to the remaining customers
    remaining_soft_tacos = 2 * (10 - 1)  # 10 customers in total, with 1 being the family

    # Calculate the total amount of money made from selling soft tacos to the remaining customers
    remaining_soft_tacos_purchase = remaining_soft_tacos * 2  # each soft taco costs $2

    # Calculate the total amount of money made during the lunch rush
    total_purchase = family_purchase + remaining_soft_tacos_purchase
    result = total_purchase
    return result

print(solution())