def solution():
    num_shirts_sold = 200
    num_minutes_sold = 25
    num_black_shirts = num_shirts_sold / 2
    num_white_shirts = num_shirts_sold / 2
    price_black_shirts = 30
    price_white_shirts = 25
    total_price = (num_black_shirts * price_black_shirts) + (num_white_shirts * price_white_shirts)
    money_made_per_minute = total_price / num_minutes_sold
    result = money_made_per_minute
    return result

print(solution())