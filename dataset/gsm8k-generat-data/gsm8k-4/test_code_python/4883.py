def solution():
    """Tim has to go to the doctor for a sporting injury.  He gets an MRI which costs $1200.  The doctor needs to examine it for 30 minutes and charges $300 per hour.  There is also a $150 fee just for being seen.  Insurance covered 80% how much did he pay?"""
    # Define the cost of the MRI, the doctor's fee, and the fee for being seen
    mri_cost = 1200
    doctor_fee = 300 / 60 * 0.5
    seen_fee = 150

    # Calculate the total cost
    total_cost = mri_cost + doctor_fee + seen_fee

    # Calculate the amount covered by insurance
    insurance_coverage = total_cost * 0.8

    # Calculate the amount Tim paid
    amount_paid = total_cost - insurance_coverage

    result = amount_paid
    return result

print(solution())