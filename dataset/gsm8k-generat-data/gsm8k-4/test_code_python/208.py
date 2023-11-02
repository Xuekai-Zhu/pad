def solution():
    """John puts $25 in his piggy bank every month for 2 years to save up for a vacation. He had to spend $400 from his piggy bank savings last week to repair his car. How many dollars are left in his piggy bank?"""
    # Define the total number of months and the monthly saving amount
    total_months = 24
    monthly_saving = 25

    # Calculate the total amount saved
    total_saved = total_months * monthly_saving

    # Subtract the amount spent on repairing the car
    remaining_amount = total_saved - 400

    # Return the remaining amount
    result = remaining_amount
    return result

print(solution())