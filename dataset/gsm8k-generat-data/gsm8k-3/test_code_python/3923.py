def solution():
    """Reginald is selling apples. He sells each apple for $1.25. He plans to use his profits to help repair his bike. His bike cost $80 and the repairs cost 25% of what his bike cost. After the repairs are paid for, 1/5 of the money he'd earned remains. How many apples did he sell?"""
    # Define the cost of each apple and the cost of the bike and repairs
    APPLE_COST = 1.25
    BIKE_COST = 80
    REPAIRS_COST = 0.25 * BIKE_COST

    # Calculate Reginald's profit
    profit = total_revenue - (BIKE_COST + REPAIRS_COST)

    # Calculate the amount of money he has left after paying for repairs
    remaining_money = profit * 0.2

    # Calculate the number of apples he sold
    apples_sold = remaining_money / APPLE_COST

    # Display the number of apples sold
    result = apples_sold
    return result

print(solution())