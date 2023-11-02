def solution():
    current_savings = 2  # Robi saves $2 in January
    for month in range(2, 7):  # Robi continues the saving pattern for 6 months
        current_savings *= 2  # Each month, Robi doubles his savings from the previous month
        total_savings = sum(range(2, current_savings, 2)) + current_savings  # Calculate the total savings so far
    result = total_savings
    return result

print(solution())