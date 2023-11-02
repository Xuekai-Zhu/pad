def solution():
    # Convert the minutes to hours by dividing by 60
    hours = 50 / 60

    # Calculate Weng's earnings by multiplying her hourly rate by the amount of hours worked
    earnings = hours * 12

    result = round(earnings, 2) # round to two decimal places
    return result

print(solution())