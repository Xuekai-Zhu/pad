def solution():
    candy_bar_price = 2
    chips_price = 0.5
    number_of_students = 5
    candy_bars_bought = 1
    chips_bought = 2
    total_price = (candy_bars_bought * candy_bar_price) + (chips_bought * chips_price)
    total_money_needed = total_price * number_of_students
    result = total_money_needed
    return result

print(solution())