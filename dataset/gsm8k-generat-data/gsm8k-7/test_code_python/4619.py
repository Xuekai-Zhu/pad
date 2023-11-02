def solution():
    sold_ounces = 8
    price_per_ounce = 9
    fine = 50

    # Calculate the total money earned from selling fool's gold
    total_earned = sold_ounces * price_per_ounce

    # Calculate the total money left after paying the fine
    total_left = total_earned - fine
    result = total_left
    return result

print(solution())