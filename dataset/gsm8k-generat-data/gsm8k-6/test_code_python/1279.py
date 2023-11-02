def solution():
    # Calculate the annual income of Bill
    annual_income = 25 * 30 * 4 * 12  # Bill earns $25/hour and works 30 hours per week, four weeks per month

    # Determine the percentage of healthcare cost the government will cover
    if annual_income < 10000:
        government_coverage = 0.9
    elif annual_income >= 10001 and annual_income <= 40000:
        government_coverage = 0.5
    elif annual_income > 50000:
        government_coverage = 0.2
    else:
        government_coverage = 0

    # Calculate the annual amount Bill will pay for health insurance
    total_cost = 500 * 12
    bill_payment = total_cost * (1 - government_coverage)
    result = bill_payment
    return result

print(solution())