def solution():
    """Reginald is selling apples. He sells each apple for $1.25. He plans to use his profits to help repair his bike. His bike cost $80 and the repairs cost 25% of what his bike cost. After the repairs are paid for, 1/5 of the money he'd earned remains. How many apples did he sell?"""
    # Define the cost of the bike and the percentage of that cost needed for repairs
    bike_cost = 80
    repair_percent = 0.25

    # Calculate the total cost of repairs
    repair_cost = bike_cost * repair_percent

    # Calculate the total earnings from selling apples
    total_earnings = (bike_cost + repair_cost) / (1/0.2)

    # Calculate the number of apples sold
    num_apples = total_earnings / 1.25

    result = round(num_apples)
    return result

print(solution())