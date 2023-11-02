def solution():
    # Define the number of roses and lilies
    roses = 20
    lilies = 3/4 * roses

    # Calculate the cost of the roses and lilies
    roses_cost = roses * 5
    lilies_cost = lilies * 10

    # Calculate the total cost of the flowers
    total_cost = roses_cost + lilies_cost
    result = total_cost
    return result

print(solution())