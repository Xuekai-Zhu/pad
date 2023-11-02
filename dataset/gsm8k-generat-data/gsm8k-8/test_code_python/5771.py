def solution():
    # Define the number of shirts and pants purchased
    num_shirts = 10
    num_pants = num_shirts / 2

    # Calculate the total cost of the shirts and pants
    shirt_cost = num_shirts * 6
    pant_cost = num_pants * 8

    # Calculate the total cost of everything
    total_cost = shirt_cost + pant_cost
    result = total_cost
    return result

print(solution())