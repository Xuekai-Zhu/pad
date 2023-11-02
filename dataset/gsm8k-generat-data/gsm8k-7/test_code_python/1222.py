def solution():
    apple_price = 1.5
    orange_price = 1
    morning_apple_sold = 40
    morning_orange_sold = 30
    afternoon_apple_sold = 50
    afternoon_orange_sold = 40

    # Calculate the total sales in the morning
    morning_sales = (morning_apple_sold * apple_price) + (morning_orange_sold * orange_price)

    # Calculate the total sales in the afternoon
    afternoon_sales = (afternoon_apple_sold * apple_price) + (afternoon_orange_sold * orange_price)

    # Calculate the total sales for the day
    total_sales = morning_sales + afternoon_sales
    result = total_sales
    return result

print(solution())