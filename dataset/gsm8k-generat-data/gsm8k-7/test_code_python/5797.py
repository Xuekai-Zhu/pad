def solution():
    num_coffee_customers = 7
    coffee_price = 5

    num_tea_customers = 8
    tea_price = 4

    # Calculate the total revenue from coffee sales
    coffee_revenue = num_coffee_customers * coffee_price

    # Calculate the total revenue from tea sales
    tea_revenue = num_tea_customers * tea_price

    # Calculate the total revenue from all sales
    total_revenue = coffee_revenue + tea_revenue
    result = total_revenue
    return result

print(solution())