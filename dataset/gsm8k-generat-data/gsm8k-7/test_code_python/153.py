def solution():
    # Calculate the amount paid for Tim's doctor's visit
    doc_visit_cost = 300
    doc_insurance_coverage = 0.75
    amount_paid_doc = doc_visit_cost * (1 - doc_insurance_coverage)

    # Calculate the amount paid for Tim's cat's visit
    cat_visit_cost = 120
    cat_insurance_coverage = 60
    amount_paid_cat = cat_visit_cost - cat_insurance_coverage

    # Calculate the total amount paid
    total_amount_paid = amount_paid_doc + amount_paid_cat
    result = total_amount_paid
    return result

print(solution())