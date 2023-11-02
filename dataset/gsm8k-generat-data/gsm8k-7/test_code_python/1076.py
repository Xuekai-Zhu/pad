def solution():
    dolls = 3
    doll_price = 5

    clocks = 2
    clock_price = 15

    glasses = 5
    glass_price = 4

    total_cost = 40

    # Calculate the total revenue from selling all items
    total_revenue = (dolls * doll_price) + (clocks * clock_price) + (glasses * glass_price)

    # Calculate the profit made
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())