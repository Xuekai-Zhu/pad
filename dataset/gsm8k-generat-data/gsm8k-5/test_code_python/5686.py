def solution():
    # Calculate total money earned from selling tees
    tees_sold = 7
    tees_price = 8
    total_tees_money = tees_sold * tees_price

    # Calculate total money earned from selling jeans
    jeans_sold = 4
    jeans_price = 11
    total_jeans_money = jeans_sold * jeans_price

    # Calculate the total money earned at the end of the day
    total_money = total_tees_money + total_jeans_money
    result = total_money
    return result

print(solution())