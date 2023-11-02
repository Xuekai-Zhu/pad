def solution():
    # Calculate the number of black and white shirts sold
    black_shirts_sold = 200 / 2
    white_shirts_sold = 200 / 2

    # Calculate the total amount of money made from black and white shirts
    total_money_black = black_shirts_sold * 30
    total_money_white = white_shirts_sold * 25
    total_money = total_money_black + total_money_white

    # Convert the total amount of money to money per minute
    money_per_minute = total_money / 25
    result = money_per_minute
    return result

print(solution())