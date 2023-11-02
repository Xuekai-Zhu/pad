def solution():
    """There are 50 staplers in the stapler. Stacie staples 3 dozen reports on her desk. How many staplers are left in the stapler?"""
    # Define the total number of staplers and the number of reports to staple
    total_staplers = 50
    reports = 3 * 12

    # Calculate the number of staplers used to staple the reports
    staplers_used = reports / 2

    # Calculate the number of staplers remaining in the stapler
    staplers_remaining = total_staplers - staplers_used

    # return the result
    result = staplers_remaining
    return result

print(solution())