def solution():
    # Define the mileage for each day
    monday_miles = 18
    tuesday_miles = 26
    wednesday_miles = 20
    thursday_miles = 20
    friday_miles = 16

    # Calculate the total mileage for the week
    total_miles = monday_miles + tuesday_miles + wednesday_miles + thursday_miles + friday_miles

    # Calculate the reimbursement amount
    reimbursement = total_miles * 0.36
    result = reimbursement
    return result

print(solution())