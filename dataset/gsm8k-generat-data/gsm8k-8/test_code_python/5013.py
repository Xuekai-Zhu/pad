def solution():
    # Define the number of staplers and reports
    staplers = 50
    reports = 3 * 12

    # Calculate the number of staplers used
    staplers_used = reports / 2  # assuming 2 staples per report

    # Calculate the number of staplers left
    staplers_left = staplers - staplers_used
    result = staplers_left
    return result

print(solution())