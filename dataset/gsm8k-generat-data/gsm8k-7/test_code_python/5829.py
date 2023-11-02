def solution():
    num_black_shirts = 100
    black_shirt_price = 30

    num_white_shirts = 100
    white_shirt_price = 25

    total_shirts_sold = 200
    total_sale_time = 25  # minutes

    # Calculate the total revenue from black shirts sold
    black_shirts_revenue = num_black_shirts * black_shirt_price

    # Calculate the total revenue from white shirts sold
    white_shirts_revenue = num_white_shirts * white_shirt_price

    # Calculate the total revenue from all shirts sold
    total_revenue = black_shirts_revenue + white_shirts_revenue

    # Calculate the revenue per minute during the sale
    revenue_per_minute = total_revenue / total_sale_time
    result = revenue_per_minute
    return result

print(solution())