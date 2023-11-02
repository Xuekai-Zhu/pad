def solution():
    # Calculate the total revenue Miguel collected
    total_revenue = 128

    # Calculate how much of the revenue comes from entrance fees
    entrance_fee_revenue = 4 * 3

    # Calculate how much revenue comes from strawberry sales
    strawberry_sales_revenue = total_revenue - entrance_fee_revenue

    # Calculate how many pounds of strawberries were picked
    pounds_picked = strawberry_sales_revenue/20
    result = pounds_picked
    return result

print(solution())