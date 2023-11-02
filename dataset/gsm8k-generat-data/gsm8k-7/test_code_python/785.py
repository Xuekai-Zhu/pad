def solution():
    total_customers = 25
    coffee_ratio = 3/5

    # Calculate the number of customers who bought coffee
    coffee_customers = total_customers * coffee_ratio

    # Calculate the number of customers who did not buy coffee
    non_coffee_customers = total_customers - coffee_customers
    result = non_coffee_customers
    return result

print(solution())