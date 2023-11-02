def solution():
    """There are 50 staplers in the stapler.  Stacie staples 3 dozen reports on her desk.  How many staplers are left in the stapler?"""
    # Define the initial number of staplers
    initial_staplers = 50

    # Define the number of reports to be stapled
    reports = 3 * 12

    # Calculate the total number of staples used
    staples_used = reports * 2  # Each report requires 2 staples

    # Calculate the number of staplers left
    staplers_left = initial_staplers - staples_used

    # Display the number of staplers left
    result = staplers_left
    return result

print(solution())