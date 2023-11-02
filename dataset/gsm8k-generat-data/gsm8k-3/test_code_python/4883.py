def solution():
    """Tim has to go to the doctor for a sporting injury. He gets an MRI which costs $1200. The doctor needs to examine it for 30 minutes and charges $300 per hour. There is also a $150 fee just for being seen. Insurance covered 80% how much did he pay?"""
    # Define the cost of the MRI
    MRI_COST = 1200

    # Define the cost of the doctor's examination, including the fee for being seen
    EXAMINATION_FEE = 150
    EXAMINATION_HOUR_RATE = 300

    # Calculate the cost of the doctor's examination
    examination_cost = EXAMINATION_FEE + (EXAMINATION_HOUR_RATE * 0.5)  # 30 minutes = 0.5 hours

    # Calculate the total cost before insurance coverage
    total_cost = MRI_COST + examination_cost

    # Apply the insurance coverage
    total_cost_after_insurance = total_cost * 0.2
    amount_paid = total_cost - total_cost_after_insurance

    # Display the amount paid after insurance coverage
    result = amount_paid
    return result

print(solution())