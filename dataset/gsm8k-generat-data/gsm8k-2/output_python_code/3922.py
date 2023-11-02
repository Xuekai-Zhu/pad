def solution():
    """Reginald is selling apples. He sells each apple for $1.25. He plans to use his profits to help repair his bike. His bike cost $80 and the repairs cost 25% of what his bike cost. After the repairs are paid for, 1/5 of the money he'd earned remains. How many apples did he sell?"""
    apple_price = 1.25
    bike_cost = 80
    repair_cost = 0.25 * bike_cost
    total_cost = bike_cost + repair_cost
    total_earnings = 5 * total_cost
    number_of_apples = int(total_earnings / apple_price)
    result = number_of_apples
    return result

print(solution())