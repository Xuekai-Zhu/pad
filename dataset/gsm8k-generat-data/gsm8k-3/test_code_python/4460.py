def solution():
    """James buys a weight vest for $250.  He then buys 200 pounds of weight plates for $1.2 per pound.  A 200-pound weight vest would cost $700 but there is a $100 discount.  How much does he save with his vest?"""
    # Define the cost of the weight vest
    VEST_COST = 250

    # Define the cost per pound of weight plates
    PLATE_COST = 1.2

    # Define the cost of a 200-pound weight vest with discount
    DISCOUNTED_VEST_COST = 700 - 100

    # Calculate the cost of the weight plates
    plate_cost = 200 * PLATE_COST

    # Calculate the total cost of James' purchase
    total_cost = VEST_COST + plate_cost

    # Calculate the amount saved with the weight vest purchase
    savings = DISCOUNTED_VEST_COST - total_cost

    # Display the amount saved
    result = savings
    return result

print(solution())