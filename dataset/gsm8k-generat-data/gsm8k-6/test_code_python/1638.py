def solution():
    # Calculate the total savings required for the down payment
    total_savings = 108000  

    # Calculate the monthly savings required by Richard and Sarah combined
    monthly_savings = total_savings / (3 * 12)  # 3 years = 36 months

    # Calculate the amount each person saves per month
    amount_per_person = monthly_savings / 2 

    result = amount_per_person
    return result

print(solution())