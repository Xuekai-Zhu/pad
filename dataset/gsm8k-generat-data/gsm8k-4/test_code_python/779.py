def solution():
    """The flowers cost $9, the clay pot costs $20 more than the flower, and the bag of soil costs $2 less than the flower. How much does it cost to plant the flowers?"""
    # Define the cost of the flowers, clay pot, and bag of soil
    flower_cost = 9
    pot_cost = flower_cost + 20
    soil_cost = flower_cost - 2

    # Calculate the total cost of planting the flowers
    total_cost = flower_cost + pot_cost + soil_cost

    # return the result
    result = total_cost
    return result

print(solution())