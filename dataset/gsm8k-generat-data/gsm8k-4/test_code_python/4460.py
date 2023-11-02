def solution():
    """James buys a weight vest for $250. He then buys 200 pounds of weight plates for $1.2 per pound. A 200-pound weight vest would cost $700 but there is a $100 discount. How much does he save with his vest?"""
    # Define the initial cost of the weight vest and the cost per pound of weight plates
    VEST_COST = 250
    WEIGHT_PLATE_COST = 1.2

    # Calculate the cost of the weight plates
    weight_plates_cost = 200 * WEIGHT_PLATE_COST

    # Calculate the potential cost of a 200-pound weight vest with the discount
    potential_vest_cost = 700 - 100

    # Calculate the total cost of James' weight vest and weight plates
    total_cost = VEST_COST + weight_plates_cost

    # Calculate the amount James saved with his weight vest
    savings = potential_vest_cost - total_cost

    result = savings
    return result

print(solution())