def solution():
    # Calculate the total savings needed over 3 years
    total_savings = 108000

    # Calculate the monthly savings needed for 3 years
    monthly_savings = total_savings / (3 * 12)

    # Calculate the amount each person needs to save per month
    amount_per_person = monthly_savings / 2
    result = amount_per_person
    return result

print(solution())