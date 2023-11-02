def solution():
    # Calculate the total amount of meat sold
    total_sold = 210 + 2*210 + 130 + 0.5*130

    # Calculate the amount of meat sold beyond their original plans
    sold_beyond_plans = total_sold - 500
    result = sold_beyond_plans
    return result

print(solution())