def solution():
    
    hard_shell_price = 5
    soft_shell_price = 2
    family_hard_shell = 4
    family_soft_shell = 3
    extra_customers = 10
    extra_customers_soft_shell = extra_customers * 2
    family_cost = (family_hard_shell * hard_shell_price) + (family_soft_shell * soft_shell_price)
    extra_customers_cost = extra_customers_soft_shell * soft_shell_price
    total_sales = family_cost + extra_customers_cost
    result = total_sales
    
    return result

print(solution())