def solution():
    
    chocolate_oranges_sold = 20
    chocolate_oranges_profit = chocolate_oranges_sold * 10
    remaining_goal = 1000 - chocolate_oranges_profit
    candy_bars_price = 5
    candy_bars_needed = remaining_goal / candy_bars_price
    result = candy_bars_needed
    return result

print(solution())