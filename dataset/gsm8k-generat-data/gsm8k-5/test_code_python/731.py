def solution():
    shirts_sold = 20
    jeans_sold = 10
    shirt_price = 10
    jeans_price = shirt_price * 2

    # Calculate the total revenue from shirt sales
    shirt_revenue = shirts_sold * shirt_price

    # Calculate the total revenue from jeans sales
    jeans_revenue = jeans_sold * jeans_price

    # Calculate the total revenue from all sales
    total_revenue = shirt_revenue + jeans_revenue
    result = total_revenue
    return result

print(solution())