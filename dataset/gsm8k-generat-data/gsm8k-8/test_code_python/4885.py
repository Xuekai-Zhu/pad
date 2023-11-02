def solution():
    # Calculate the amount spent on living expenses
    living_expenses = 0.75 * 1600

    # Calculate the amount spent on insurance
    insurance = 1600 / 5

    # Calculate the amount saved
    saved = 1600 - living_expenses - insurance

    result = saved
    return result

print(solution())