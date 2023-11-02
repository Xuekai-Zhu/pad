def solution():
    # Calculate how many limes Julio will need for 30 days, assuming he uses 1 lime per day
    limes_per_day = 1 / 2  # Because he can get 2 tablespoons of juice per lime
    limes_for_30_days = limes_per_day * 30

    # Calculate how many dollars Julio will spend on limes
    limes_price = 1 / 3  # Because 3 limes cost $1.00
    total_limes_cost = limes_price * limes_for_30_days

    result = total_limes_cost
    return result

print(solution())