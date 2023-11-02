def solution():
    num_hard_shell_tacos = 4
    hard_shell_taco_price = 5

    num_soft_tacos_family = 3
    num_hard_tacos_family = 4
    soft_taco_price = 2

    num_customers_after_family = 10
    num_soft_tacos_per_customer = 2

    # Calculate the total sales from the family
    sales_family = (num_hard_shell_tacos * hard_shell_taco_price) + (num_soft_tacos_family * soft_taco_price)

    # Calculate the total sales from the rest of the customers
    num_soft_tacos_rest = num_customers_after_family * num_soft_tacos_per_customer
    sales_rest = num_soft_tacos_rest * soft_taco_price

    # Calculate the total sales during the lunch rush
    total_sales = sales_family + sales_rest
    result = total_sales
    return result

print(solution())