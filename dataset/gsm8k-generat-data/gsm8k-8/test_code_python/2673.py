def solution():
    # Define the initial savings and the monthly increase
    initial_savings = 10
    monthly_increase = 30

    # Calculate Alice's total savings after three months
    total_savings = initial_savings + monthly_increase + monthly_increase + initial_savings + 2 * monthly_increase

    result = total_savings
    return result

print(solution())