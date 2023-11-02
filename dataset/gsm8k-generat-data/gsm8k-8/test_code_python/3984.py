def solution():
    # Define Judson's contribution
    judson_contribution = 500

    # Calculate Kenny's contribution
    kenny_contribution = judson_contribution * 1.2

    # Calculate Camilo's contribution
    camilo_contribution = kenny_contribution + 200

    # Calculate the total cost of painting the house
    total_cost = judson_contribution + kenny_contribution + camilo_contribution
    result = total_cost
    return result

print(solution())