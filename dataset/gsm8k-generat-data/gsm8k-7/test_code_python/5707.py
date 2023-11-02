def solution():
    num_red_stamps = 20
    red_price = 1.1

    num_blue_stamps = 80
    blue_price = 0.8

    num_yellow_stamps = 7

    total_sale = 100

    # Calculate the total earned from selling red and blue stamps
    earned_from_red_stamps = num_red_stamps * red_price
    earned_from_blue_stamps = num_blue_stamps * blue_price
    total_earned = earned_from_red_stamps + earned_from_blue_stamps

    # Calculate the total amount needed to earn from selling yellow stamps
    yellow_sale_amount = total_sale - total_earned

    # Calculate the price needed to sell one yellow stamp to make the desired amount
    yellow_price = yellow_sale_amount / num_yellow_stamps
    result = yellow_price
    return result

print(solution())