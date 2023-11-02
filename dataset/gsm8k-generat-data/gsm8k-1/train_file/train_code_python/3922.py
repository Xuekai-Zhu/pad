def solution():
    """Reginald is selling apples. He sells each apple for $1.25. He plans to use his profits to help repair his bike. His bike cost $80 and the repairs cost 25% of what his bike cost. After the repairs are paid for, 1/5 of the money he'd earned remains. How many apples did he sell?"""
    apple_price = 1.25
    bike_cost = 80
    repair_cost = bike_cost * 0.25
    total_cost = bike_cost + repair_cost
    total_revenue = total_cost * 5
    apples_sold = total_revenue / apple_price
    result = apples_sold
    return result

print(solution())