def solution():
    normal_price = 30
    promo_rate = 1/3
    extra_fee = 15

    # Calculate the cost for the first month with promotional rate
    promo_price = normal_price * promo_rate
    first_month_price = promo_price + normal_price

    # Calculate the cost for the next 3 months without promo rate
    next_3_months_price = normal_price * 3

    # Calculate the cost for the 5th and 6th month
    extra_fee_months_price = normal_price + extra_fee

    # Calculate the total cost for 6 months
    total_cost = first_month_price + next_3_months_price + extra_fee_months_price
    result = total_cost
    return result

print(solution())