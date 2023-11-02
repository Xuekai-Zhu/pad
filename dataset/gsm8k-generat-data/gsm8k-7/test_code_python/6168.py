def solution():
    num_apples = 50
    apple_price = 0.80

    num_oranges = 40
    orange_price = 0.50

    # Calculate the total revenue from the apples sold
    apples_sold = num_apples - 10
    total_apple_revenue = apples_sold * apple_price

    # Calculate the total revenue from the oranges sold
    oranges_sold = num_oranges - 6
    total_orange_revenue = oranges_sold * orange_price

    # Calculate the total revenue from the sale of apples and oranges
    total_revenue = total_apple_revenue + total_orange_revenue
    result = total_revenue
    return result

print(solution())