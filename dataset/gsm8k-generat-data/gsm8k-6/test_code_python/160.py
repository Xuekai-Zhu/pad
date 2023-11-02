def solution():
    # Calculate the total cost of burgers
    burgers_cost = 100 * 3

    # Calculate the total cost of condiments and propane
    extra_cost = 80

    # Calculate the total cost of everything
    total_cost = burgers_cost + extra_cost + 200

    # Divide the total cost by 4 to find John's share
    john_share = total_cost / 4

    result = john_share
    return result

print(solution())