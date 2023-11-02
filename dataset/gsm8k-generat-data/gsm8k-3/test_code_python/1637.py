def solution():
    """Lennon is a sales rep and is paid $0.36 in mileage reimbursement when he travels to meet with clients.  On Monday he drove 18 miles.  Tuesday he drove 26 miles.  Wednesday and Thursday he drove 20 miles each day and on Friday he drove 16 miles.  How much money will he be reimbursed?"""
    # Define the mileage reimbursement rate
    REIMBURSEMENT_RATE = 0.36
    
    # Define the number of miles driven each day
    monday_miles = 18
    tuesday_miles = 26
    wednesday_miles = 20
    thursday_miles = 20
    friday_miles = 16
    
    # Calculate the total miles driven for the week
    total_miles = monday_miles + tuesday_miles + wednesday_miles + thursday_miles + friday_miles
    
    # Calculate the total reimbursement for the week
    total_reimbursement = total_miles * REIMBURSEMENT_RATE
    
    # Display the total reimbursement
    result = total_reimbursement
    return result

print(solution())