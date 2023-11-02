def solution():
    judson_contribution = 500  # Judson contributed $500
    kenny_contribution = 1.2 * judson_contribution  # Kenny contributed 20% more than Judson
    camilo_contribution = kenny_contribution + 200  # Camilo contributed $200 more than Kenny

    # Calculate the total amount contributed by all three
    total_contribution = judson_contribution + kenny_contribution + camilo_contribution

    # Assume that the cost of painting the house is equal to the total contribution
    cost_of_painting = total_contribution
    result = cost_of_painting
    return result

print(solution())