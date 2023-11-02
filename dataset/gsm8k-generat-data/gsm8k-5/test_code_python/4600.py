def solution():
    chocolate_oranges_sold = 20  # Nick sold out of 20 chocolate oranges
    chocolate_oranges_sales = chocolate_oranges_sold * 10  # Nick sold each chocolate orange for $10
    remaining_sales_goal = 1000 - chocolate_oranges_sales  # Nick's total sales goal is $1000
    candy_bars_price = 5  # Nick is selling each candy bar for $5

    # Calculate the number of candy bars Nick needs to sell
    candy_bars_sold = remaining_sales_goal / candy_bars_price
    result = candy_bars_sold
    return result

print(solution())