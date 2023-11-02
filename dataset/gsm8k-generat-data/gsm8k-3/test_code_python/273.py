def solution():
    """Nadia was sent to the flower shop to buy 20 roses and 3/4 times as many Lillies as roses. If roses cost $5 each and lilies cost twice as much each, calculate the total amount of money Nadia used to buy the flowers."""
    # Define the cost of roses and lilies
    ROSE_COST = 5
    LILY_COST = 2 * ROSE_COST

    # Define the number of roses and lilies purchased
    roses = 20
    lilies = 3/4 * roses

    # Calculate the total cost of the roses and lilies
    rose_cost = roses * ROSE_COST
    lily_cost = lilies * LILY_COST

    # Calculate the total cost of all the flowers
    total_cost = rose_cost + lily_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())