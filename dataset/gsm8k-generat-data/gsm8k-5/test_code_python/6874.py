def solution():
    normal_price = 30  # Mandy normally pays $30 per month for data
    promo_price = normal_price / 3  # Mandy got a promotional rate of one-third the normal price
    extra_fee = 15  # Mandy was charged an extra fee of $15 in the fourth month
    months = 6  # Mandy wants to know how much she paid in the first 6 months

    # Calculate the total cost for the first 6 months
    total_cost = promo_price + (normal_price * 3) + extra_fee

    result = total_cost
    return result

print(solution())