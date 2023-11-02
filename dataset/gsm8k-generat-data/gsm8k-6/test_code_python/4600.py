def solution():
    # Calculate the total amount of money raised from selling chocolate oranges
    chocolate_oranges = 20
    chocolate_oranges_sales = 10 * chocolate_oranges

    # Calculate the amount of money needed to be raised from selling candy bars
    candy_bars_sales = 1000 - chocolate_oranges_sales

    # Calculate the number of candy bars needed to be sold
    candy_bars = candy_bars_sales / 5
    result = candy_bars
    return result

print(solution())