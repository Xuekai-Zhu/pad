def solution():
    
    monday_miles = 18
    tuesday_miles = 26
    wednesday_miles = 20
    thursday_miles = 20
    friday_miles = 16
    total_miles = monday_miles + tuesday_miles + wednesday_miles + thursday_miles + friday_miles
    mileage_reimbursement = total_miles * 0.36
    result = mileage_reimbursement
    return result

print(solution())