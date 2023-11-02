def solution():
    # Calculate the total number of pills taken
    total_pills = 9 * 14

    # Calculate the cost of the four pills that cost $1.50 each
    four_pills_cost = 4 * 1.5

    # Calculate the cost of the remaining pills
    remaining_pills_cost = (total_pills - 4) * 5.5

    # Calculate the total cost of all the pills
    total_cost = four_pills_cost + remaining_pills_cost
    result = total_cost
    return result

print(solution())