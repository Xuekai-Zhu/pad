def solution():
    # Define the variables
    time = 3  # years
    down_payment = 108000
    total_savings = down_payment / time  # Total savings needed per person (assuming equal contribution)

    # Calculate the monthly savings per person
    monthly_savings_per_person = total_savings / 36  # 36 months in 3 years
    result = monthly_savings_per_person
    return result

print(solution())