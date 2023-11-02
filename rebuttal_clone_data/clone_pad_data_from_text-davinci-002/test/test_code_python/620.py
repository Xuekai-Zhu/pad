def solution():
    dolls_sold = 3
    clocks_sold = 2
    glasses_sold = 5
    doll_price = 5
    clock_price = 15
    glass_price = 4
    total_cost = 40
    total_revenue = (dolls_sold * doll_price) + (clocks_sold * clock_price) + (glasses_sold * glass_price)
    profit = total_revenue - total_cost

    return profit

print(solution())