def solution():
    jayda_spending = 400  # Jayda spent $400
    aitana_spending = (2 / 5) * jayda_spending + jayda_spending  # Aitana spent 2/5 times more than Jayda

    # Calculate the total amount of money they spent together
    total_spending = jayda_spending + aitana_spending
    result = total_spending
    return result

print(solution())