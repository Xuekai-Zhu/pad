def solution():
    # Define the costs of each item
    burger_cost = 5
    sandwich_cost = 4
    smoothie_cost = 4

    # Calculate the total cost of the order
    total_cost = burger_cost + sandwich_cost + (smoothie_cost * 2)

    result = total_cost
    return result

print(solution())