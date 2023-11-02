def solution():
    avg_bacon_per_pig = 20
    price_per_pound = 6
    size_ratio = 0.5  # runt sized pig

    # Calculate the total bacon the runt pig produces
    bacon_from_runt = avg_bacon_per_pig * size_ratio

    # Calculate the total amount of money the farmer makes from selling the bacon
    total_income = bacon_from_runt * price_per_pound
    result = total_income
    return result

print(solution())