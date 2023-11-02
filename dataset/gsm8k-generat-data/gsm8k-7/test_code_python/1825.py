def solution():
    months_insured = 24
    monthly_insurance_cost = 20
    procedure_cost = 5000
    insurance_coverage = 0.8

    total_insurance_cost = months_insured * monthly_insurance_cost
    covered_procedure_cost = procedure_cost * insurance_coverage
    amount_paid_with_insurance = total_insurance_cost + (procedure_cost - covered_procedure_cost)

    amount_paid_without_insurance = procedure_cost

    amount_saved_with_insurance = amount_paid_without_insurance - amount_paid_with_insurance
    result = amount_saved_with_insurance
    return result

print(solution())