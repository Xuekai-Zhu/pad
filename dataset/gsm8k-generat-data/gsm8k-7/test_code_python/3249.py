def solution():
    strawberry_cost = 2.20
    cherry_cost = 6 * strawberry_cost
    num_strawberries = 5
    num_cherries = 5

    # Calculate the total cost of strawberries
    strawberry_total_cost = num_strawberries * strawberry_cost

    # Calculate the total cost of cherries
    cherry_total_cost = num_cherries * cherry_cost

    # Calculate the total cost of both strawberries and cherries
    total_cost = strawberry_total_cost + cherry_total_cost
    result = total_cost
    return result

print(solution())