def solution():
    num_shirts = 20
    shirt_price = 10

    num_jeans = 10
    jeans_price = 2 * shirt_price

    # Calculate the total revenue from selling all shirts
    total_shirt_revenue = num_shirts * shirt_price

    # Calculate the total revenue from selling all jeans
    total_jeans_revenue = num_jeans * jeans_price

    # Calculate the total revenue from selling all clothing items
    total_revenue = total_shirt_revenue + total_jeans_revenue
    result = total_revenue
    return result

print(solution())