def solution():
    rate_per_hour = 14
    num_hours_per_day = 2
    num_days_per_week = 7
    shoes_cost = 0
    mom_share = 0

    # Calculate the total number of hours David mowed for
    total_hours_mowed = num_hours_per_day * num_days_per_week

    # Calculate the total money David made from mowing
    total_money_made = total_hours_mowed * rate_per_hour

    # Calculate the cost of the shoes David bought
    shoes_cost = total_money_made / 2

    # Calculate the amount of money David gave to his mom
    mom_share = (total_money_made - shoes_cost) / 2

    # Calculate how much money David has left
    money_left = total_money_made - shoes_cost - mom_share
    result = money_left
    return result

print(solution())