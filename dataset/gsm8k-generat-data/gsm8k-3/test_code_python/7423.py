def solution():
    """A sack of rice, which is 50 kilograms,  costs $50. If David sells it for $1.20 per kilogram, how much will be his profit?"""
    # Define the cost of the sack of rice and the selling price per kilogram
    COST = 50
    SELLING_PRICE = 1.20

    # Calculate the total revenue from selling the rice
    revenue = SELLING_PRICE * 50

    # Calculate the profit
    profit = revenue - COST

    # Display the profit
    result = profit
    return result

print(solution())