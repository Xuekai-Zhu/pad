def solution():
    total_months = 6
    current_savings = 2
    total_savings = current_savings

    # Calculate the savings for the next 3 months and add it to the total savings
    for i in range(2, 5):
        current_savings *= 2
        total_savings += current_savings

    result = total_savings
    return result

print(solution())