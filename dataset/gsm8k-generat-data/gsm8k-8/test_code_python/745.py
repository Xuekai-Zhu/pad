def solution():
    # Define the quantities and prices
    num_customers = 500
    lettuce_price = 1
    lettuce_quantity = 2
    tomato_price = 0.5
    tomato_quantity = 4

    # Calculate the total sales for each item
    lettuce_sales = num_customers * lettuce_price * lettuce_quantity
    tomato_sales = num_customers * tomato_price * tomato_quantity

    # Calculate the total sales for both items
    total_sales = lettuce_sales + tomato_sales
    result = total_sales
    return result

print(solution())