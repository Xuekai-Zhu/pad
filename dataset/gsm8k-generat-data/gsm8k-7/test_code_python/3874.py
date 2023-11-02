def solution():
    cakes_per_day = 4
    price_per_cake = 8
    weekdays = 5
    weeks = 4

    # Calculate the total number of cakes made in 4 weeks
    total_cakes_made = cakes_per_day * weekdays * weeks

    # Calculate the total amount of money collected from selling all the cakes
    total_money_collected = total_cakes_made * price_per_cake
    result = total_money_collected
    return result

print(solution())