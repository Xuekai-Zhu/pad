def solution():
    judson_money = 500
    kenny_money = judson_money * 1.2
    camilo_money = kenny_money + 200

    # Calculate the total amount of money contributed by all three
    total_money = judson_money + kenny_money + camilo_money

    # Assuming the cost of painting the house is equal to the total amount of money contributed
    cost_of_painting = total_money
    result = cost_of_painting
    return result

print(solution())