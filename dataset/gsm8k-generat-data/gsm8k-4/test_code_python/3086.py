def solution():
    """A retail store wants to hire 50 new phone reps to assist with the increased call volume that they will experience over the holiday. Each phone rep will work 8 hours a day and will be paid $14.00 an hour. After 5 days, how much will the company pay all 50 new employees?"""
    # Define the number of phone reps to be hired
    num_reps = 50

    # Define the number of hours each rep will work per day
    hours_per_day = 8

    # Define the hourly wage for each rep
    hourly_wage = 14.00

    # Calculate the total cost of paying all 50 new employees for 5 days
    total_pay = num_reps * hours_per_day * hourly_wage * 5

    # Return the result
    result = total_pay
    return result

print(solution())