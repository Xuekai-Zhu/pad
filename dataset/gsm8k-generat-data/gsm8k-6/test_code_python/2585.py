def solution():
    full_price = 85  # full price of shoes
    discount_1yr = 0.2  # discount for officers who served at least 1 year
    discount_3yr = 0.25  # additional discount for officers who served at least 3 years

    first_discount_price = full_price * (1 - discount_1yr)  # price after 1st discount
    final_price = first_discount_price * (1 - discount_3yr)  # price after final discount

    result = final_price
    return result

print(solution())