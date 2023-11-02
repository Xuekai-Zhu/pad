def solution():
    # Calculate the amount covered by insurance for Tim's doctor's visit
    doc_insurance_coverage = 0.75
    doc_insurance_pay = 300 * doc_insurance_coverage

    # Calculate the amount covered by insurance for Tim's cat's visit
    cat_insurance_coverage = 60
    cat_insurance_pay = 120 - cat_insurance_coverage
    
    # Calculate the total amount Tim paid
    total_paid = 300 - doc_insurance_pay + 120 - cat_insurance_pay
    result = total_paid
    return result

print(solution())