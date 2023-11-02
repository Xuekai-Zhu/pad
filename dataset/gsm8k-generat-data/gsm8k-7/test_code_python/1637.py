def solution():
    monday_miles = 18
    tuesday_miles = 26
    wednesday_miles = 20
    thursday_miles = 20
    friday_miles = 16
    mileage_reimbursement = 0.36

    # Calculate the total number of miles driven
    total_miles = monday_miles + tuesday_miles + wednesday_miles + thursday_miles + friday_miles

    # Calculate the total reimbursement amount
    reimbursement_amount = total_miles * mileage_reimbursement
    result = reimbursement_amount
    return result

print(solution())