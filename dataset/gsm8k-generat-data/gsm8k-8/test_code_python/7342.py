def solution():
    # Define the original cost of one shirt
    original_cost = 10

    # Calculate the cost of buying two shirts
    two_shirt_cost = original_cost + 0.5 * original_cost

    # Calculate the cost of buying three shirts
    three_shirt_cost = two_shirt_cost + 0.6 * original_cost

    # Calculate the amount saved
    amount_saved = (3 * original_cost) - three_shirt_cost
    result = amount_saved
    return result

print(solution())