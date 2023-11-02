def solution():
    # Calculate the cost of buying individual carnations
    individual_carnation_cost = 0.5

    # Calculate the cost of buying a dozen carnations
    dozen_carnation_cost = 4.0

    # Calculate the total number of carnations needed
    total_carnations = 5 * 12 + 14

    # Calculate the number of dozens of carnations needed
    dozens_needed = total_carnations // 12

    # Calculate the number of individual carnations needed
    individual_carnations_needed = total_carnations % 12

    # Calculate the total cost of buying carnations
    total_cost = dozens_needed * dozen_carnation_cost + individual_carnations_needed * individual_carnation_cost
    result = total_cost
    return result

print(solution())