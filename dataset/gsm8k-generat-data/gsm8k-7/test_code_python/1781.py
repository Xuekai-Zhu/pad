def solution():
    num_backpacks = 48
    total_cost = 576

    num_sold_swap_meet = 17
    price_sold_swap_meet = 18

    num_sold_dept_store = 10
    price_sold_dept_store = 25

    # Calculate the number of backpacks sold at the higher price
    num_sold_high_price = num_sold_swap_meet + num_sold_dept_store
    # Calculate the number of backpacks remaining
    num_remaining = num_backpacks - num_sold_high_price

    # Calculate the total revenue from selling backpacks at different prices
    total_revenue = (num_sold_swap_meet * price_sold_swap_meet) + (num_sold_dept_store * price_sold_dept_store) + (num_remaining * 22)

    # Calculate the profit
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())