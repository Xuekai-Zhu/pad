def solution():
    # Calculate the amount Jade spends on living expenses
    living_expenses = 0.75 * 1600

    # Calculate the amount Jade spends on insurance
    insurance = (1/5) * 1600

    # Calculate the amount Jade saves
    savings = 1600 - living_expenses - insurance

    result = savings
    return result

print(solution())