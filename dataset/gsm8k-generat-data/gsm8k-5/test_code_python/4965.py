def solution():
    first_shirt_cost = 15  # The first shirt costs $15
    second_shirt_cost = first_shirt_cost - 6  # The second shirt costs $6 less than the first shirt
    total_cost = 2 * (first_shirt_cost + second_shirt_cost)  # John bought 2 shirts, so the total cost is twice the sum of the costs of the two shirts

    result = total_cost
    return result

print(solution())