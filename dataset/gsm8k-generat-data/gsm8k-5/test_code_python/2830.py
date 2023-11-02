def solution():
    total_savings = 0
    initial_money = 2  # Derek puts $2 away in January

    # Calculate Derek's total savings by adding the amount saved each month
    for i in range(12):
        total_savings += initial_money
        initial_money *= 2  # Derek doubles the amount he saves each month

    result = total_savings
    return result

print(solution())