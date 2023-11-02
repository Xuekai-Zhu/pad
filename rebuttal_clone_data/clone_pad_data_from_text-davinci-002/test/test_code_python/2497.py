def solution():
    cost_house = 480000
    cost_trailer = 120000
    loan_term_house = 20
    loan_term_trailer = 20
    monthly_payment_house = cost_house / (loan_term_house * 12)
    monthly_payment_trailer = cost_trailer / (loan_term_trailer * 12)
    difference = monthly_payment_house - monthly_payment_trailer
    result = difference
    return result

print(solution())