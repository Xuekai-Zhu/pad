def solution():
    perfume_cost = 50.0

    christian_savings = 5.0
    christian_income = 4 * 5.0  # mowing 4 yards for $5 each

    sue_savings = 7.0
    sue_income = 6 * 2.0  # walking 6 dogs for $2 each

    # Calculate the total money they have now
    total_money = christian_savings + christian_income + sue_savings + sue_income

    # Calculate the difference between the total money they have and the perfume cost
    difference = perfume_cost - total_money
    result = difference
    return result

print(solution())