def solution():
    jeans_price = 11
    tees_price = 8

    num_jeans = 4
    num_tees = 7

    # Calculate the total revenue from selling jeans
    total_jeans_revenue = num_jeans * jeans_price

    # Calculate the total revenue from selling tees
    total_tees_revenue = num_tees * tees_price

    # Calculate the total revenue for the day
    total_revenue = total_jeans_revenue + total_tees_revenue

    # Calculate the money Linda had at the end of the day
    money_at_end_of_day = total_revenue
    result = money_at_end_of_day
    return result

print(solution())