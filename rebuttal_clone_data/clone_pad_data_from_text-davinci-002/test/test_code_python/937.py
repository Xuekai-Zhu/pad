def solution():
    monday_miles = 18
    tuesday_miles = 26
    wednesday_miles = 20
    thursday_miles = 20
    friday_miles = 16
    reimbursement_rate = 0.36
    total_reimbursement = (monday_miles + tuesday_miles + wednesday_miles + thursday_miles + friday_miles) * reimbursement_rate
    result = total_reimbursement
    return result

print(solution())