def solution():
    # Define the price of a fantasy book and the price of a literature book
    fantasy_price = 4
    literature_price = 2

    # Calculate the total sales from fantasy books and literature books
    fantasy_sales = 5 * fantasy_price * 5
    literature_sales = 8 * literature_price * 5 * 5

    # Calculate the total earnings over 5 days
    total_earnings = fantasy_sales + literature_sales
    result = total_earnings
    return result

print(solution())