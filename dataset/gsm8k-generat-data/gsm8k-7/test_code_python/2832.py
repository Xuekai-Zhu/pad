def solution():
    num_cakes = 453
    cake_price = 12.0

    num_pies = 126
    pie_price = 7.0

    # Calculate the total revenue from selling cakes
    total_cake_revenue = num_cakes * cake_price

    # Calculate the total revenue from selling pies
    total_pie_revenue = num_pies * pie_price

    # Calculate the total revenue from selling all items
    total_revenue = total_cake_revenue + total_pie_revenue
    result = total_revenue
    return result

print(solution())