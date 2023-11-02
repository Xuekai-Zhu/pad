def solution():
    """Hannah bought 3 sweatshirts and 2 T-shirts. Each sweatshirt cost 15$ and each t-shirt cost 10$. How much money did Hannah spend in all?"""
    # Define the cost of each item
    SWEATSHIRT_COST = 15
    TSHIRT_COST = 10

    # Define the number of each item purchased
    sweatshirts = 3
    tshirts = 2

    # Calculate the total cost of the sweatshirts
    sweatshirt_cost = sweatshirts * SWEATSHIRT_COST

    # Calculate the total cost of the T-shirts
    tshirt_cost = tshirts * TSHIRT_COST

    # Calculate the total cost of all the items
    total_cost = sweatshirt_cost + tshirt_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())