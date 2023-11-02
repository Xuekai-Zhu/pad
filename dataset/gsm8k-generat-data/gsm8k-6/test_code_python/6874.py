def solution():
    # Calculate the total cost of Mandy's data plan for the first 6 months
    promo_rate = 30/3  # promotional rate for the first month
    normal_rate = 30  # normal rate for the next 2 months
    extra_fee = 15  # charged in the fourth month for going over the data limit
    total_cost = promo_rate + (2 * normal_rate) + extra_fee  # total cost for the first 4 months
    result = total_cost + (2 * normal_rate)  # add cost for the next 2 months
    return result

print(solution())