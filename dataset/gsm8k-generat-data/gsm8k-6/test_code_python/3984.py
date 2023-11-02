def solution():
    # Calculate the total amount of money contributed by the three friends
    judson_money = 500
    kenny_money = 1.2 * 500  # Kenny contributed 20% more than Judson
    camilo_money = kenny_money + 200  # Camilo contributed $200 more than Kenny
    total_money = judson_money + kenny_money + camilo_money

    # Assume that the cost of painting the house is equal to the total amount of money contributed
    result = total_money
    return result

print(solution())