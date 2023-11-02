def solution():
    num_customers = 500
    num_lettuce_per_customer = 2
    lettuce_price = 1
    num_tomatoes_per_customer = 4
    tomato_price = 0.5

    # Calculate the total number of heads of lettuce sold per month
    total_lettuce = num_customers * num_lettuce_per_customer

    # Calculate the total amount of money made from selling lettuce per month
    lettuce_sales = total_lettuce * lettuce_price

    # Calculate the total number of tomatoes sold per month
    total_tomatoes = num_customers * num_tomatoes_per_customer

    # Calculate the total amount of money made from selling tomatoes per month
    tomato_sales = total_tomatoes * tomato_price

    # Calculate the total amount of money made from selling both lettuce and tomatoes per month
    total_sales = lettuce_sales + tomato_sales
    result = total_sales
    return result

print(solution())