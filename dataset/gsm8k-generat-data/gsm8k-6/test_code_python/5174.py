def solution():
    inches_to_grow = 54 - 48  # Alex needs to grow 6 inches to be tall enough
    inches_per_month = 1/3  # Alex normally grows 1/3 of an inch per month
    hours_per_inch = 12  # Alex needs to hang upside down for 12 hours to grow 1 inch

    # Calculate the number of hours Alex needs to hang upside down each month
    hours_per_month = inches_to_grow / inches_per_month * hours_per_inch
    result = hours_per_month
    return result

print(solution())