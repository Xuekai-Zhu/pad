def solution():
    num_red_stamps = 30
    red_stamp_price = 0.5

    num_white_stamps = 80
    white_stamp_price = 0.2

    # Calculate the total revenue from selling red stamps
    red_stamps_revenue = num_red_stamps * red_stamp_price

    # Calculate the total revenue from selling white stamps
    white_stamps_revenue = num_white_stamps * white_stamp_price

    # Calculate the difference in revenue between red and white stamps
    revenue_difference = red_stamps_revenue - white_stamps_revenue
    result = revenue_difference
    return result

print(solution())