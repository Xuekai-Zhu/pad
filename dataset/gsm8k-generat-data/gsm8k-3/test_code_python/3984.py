def solution():
    """Judson, Camilo, and Kenny decided to contribute money to paint their house. Judson contributed $500, Kenny contributed 20% more money than Judson, and Camilo contributed $200 more than Kenny. How much was the cost of painting the house?"""
    # Define Judson's contribution
    judson_contribution = 500

    # Calculate Kenny's contribution
    kenny_contribution = judson_contribution * 1.2

    # Calculate Camilo's contribution
    camilo_contribution = kenny_contribution + 200

    # Calculate the total amount contributed
    total_contribution = judson_contribution + kenny_contribution + camilo_contribution

    # Display the total cost
    result = total_contribution
    return result

print(solution())