def solution():
    insurance_months = 24  # Tom had pet insurance for 24 months
    insurance_cost = 20  # The insurance cost $20 per month
    procedure_cost = 5000  # Procedure cost $5000
    insurance_coverage = 0.8  # Insurance covers 80% of the procedure cost

    # Calculate the total cost of insurance for 24 months
    total_insurance_cost = insurance_months * insurance_cost

    # Calculate the amount Tom has to pay after insurance coverage
    out_of_pocket_cost = procedure_cost * (1 - insurance_coverage)

    # Calculate the total savings due to insurance
    total_savings = procedure_cost - out_of_pocket_cost - total_insurance_cost
    result = total_savings
    return result

print(solution())