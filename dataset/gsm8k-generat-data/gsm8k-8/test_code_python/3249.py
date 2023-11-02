def solution():
    # Define the cost of a pound of strawberries
    strawberry_cost = 2.20

    # Calculate the cost of a pound of cherries
    cherry_cost = 6 * strawberry_cost

    # Calculate the cost of 5 pounds of strawberries
    strawberry_total_cost = 5 * strawberry_cost

    # Calculate the cost of 5 pounds of cherries
    cherry_total_cost = 5 * cherry_cost

    # Calculate the total cost of the purchase
    total_cost = strawberry_total_cost + cherry_total_cost
    result = total_cost
    return result

print(solution())