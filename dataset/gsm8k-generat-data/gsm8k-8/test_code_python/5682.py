def solution():
    # Calculate the total sales for each item
    suits_sales = 2 * 700
    shirts_sales = 6 * 50
    loafers_sales = 2 * 150

    # Calculate the total sales for the day
    total_sales = suits_sales + shirts_sales + loafers_sales

    # Calculate the commission earned by Enrique
    commission = total_sales * 0.15
    result = commission
    return result

print(solution())