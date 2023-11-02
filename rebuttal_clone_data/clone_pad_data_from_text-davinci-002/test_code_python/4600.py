def solution():
    money_raised = 1000
    candy_bar_price = 5
    chocolate_orange_price = 10
    money_raised_from_chocolate_oranges = 20 * chocolate_orange_price
    money_needed_from_candy_bars = money_raised - money_raised_from_chocolate_oranges
    candy_bars_needed = money_needed_from_candy_bars / candy_bar_price
    result = candy_bars_needed
    return result

print(solution())