def solution():
    """Lennon is a sales rep and is paid $0.36 in mileage reimbursement when he travels to meet with clients. On Monday he drove 18 miles. Tuesday he drove 26 miles. Wednesday and Thursday he drove 20 miles each day and on Friday he drove 16 miles. How much money will he be reimbursed?"""
    # Define the mileage reimbursement rate
    REIMBURSEMENT_RATE = 0.36

    # Define the number of miles driven each day
    miles_monday = 18
    miles_tuesday = 26
    miles_wednesday = 20
    miles_thursday = 20
    miles_friday = 16

    # Calculate the total miles driven
    total_miles = miles_monday + miles_tuesday + miles_wednesday + miles_thursday + miles_friday

    # Calculate the total reimbursement
    total_reimbursement = total_miles * REIMBURSEMENT_RATE

    # Return the result
    result = total_reimbursement
    return result

print(solution())