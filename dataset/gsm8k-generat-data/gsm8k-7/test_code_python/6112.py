def solution():
    manicure_cost = 30
    tip_percentage = 0.3  # 30% tip

    # Calculate the amount of tip
    tip_amount = manicure_cost * tip_percentage

    # Calculate the total amount paid
    total_amount = manicure_cost + tip_amount
    result = total_amount
    return result

print(solution())