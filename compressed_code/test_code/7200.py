def solution():
    
    backpacks_per_case = 48
    cost_per_case = 576
    backpacks_sold_swap_meet = 17
    price_per_backpack_swap_meet = 18
    backpacks_sold_department_store = 10
    price_per_backpack_department_store = 25
    price_per_backpack_remainder = 22
    
    revenue_swap_meet = backpacks_sold_swap_meet * price_per_backpack_swap_meet
    revenue_department_store = backpacks_sold_department_store * price_per_backpack_department_store
    backpacks_remainder = backpacks_per_case - backpacks_sold_swap_meet - backpacks_sold_department_store
    revenue_remainder = backpacks_remainder * price_per_backpack_remainder
    
    total_revenue = revenue_swap_meet + revenue_department_store + revenue_remainder
    profit = total_revenue - cost_per_case
    
    result = profit
    return result

print(solution())