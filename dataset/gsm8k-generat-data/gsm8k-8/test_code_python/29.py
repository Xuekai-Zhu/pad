def solution():
    # Define the original percentage and the new percentage
    original_percent = 0.4
    new_percent = 0.25

    # Define the increase in salary
    increase = 600

    # Solve for the original income using a proportion
    original_income = (original_percent / new_percent) * (increase + (original_percent * increase))

    result = original_income
    return result

print(solution())