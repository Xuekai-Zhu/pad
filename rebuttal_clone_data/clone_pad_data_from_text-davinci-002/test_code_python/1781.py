def solution():
    backpacks_bought = 48
    backpacks_sold_at_swap_meet = 17
    backpacks_sold_to_department_store = 10
    backpacks_sold_at_regular_price = backpacks_bought - backpacks_sold_at_swap_meet - backpacks_sold_to_department_store
    profit_from_swap_meet = backpacks_sold_at_swap_meet * 18
    profit_from_department_store = backpacks_sold_to_department_store * 25
    profit_from_regular_price = backpacks_sold_at_regular_price * 22
    total_profit = profit_from_swap_meet + profit_from_department_store + profit_from_regular_price
    result = total_profit
    return result

print(solution())