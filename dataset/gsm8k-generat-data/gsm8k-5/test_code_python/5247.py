def solution():
    cost_grant = 200  # Grant spends $200 per year to have the newspaper delivered daily
    cost_juanita = (6 * 0.5 + 1 * 2) * 365  # Juanita spends $0.50 Monday-Saturday and $2.00 on Sunday
                                           # Multiplying by 365 days in a year gives yearly cost

    # Calculate the difference in cost between Juanita and Grant
    difference = cost_juanita - cost_grant
    result = difference
    return result

print(solution())