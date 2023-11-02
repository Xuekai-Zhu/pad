def solution():
    """Thomas, Toby, and Rebecca worked a total of 157 hours in one week. Thomas worked x hours. Toby worked 10 hours less than twice what Thomas worked, and Rebecca worked 8 hours less than Toby. How many hours did Rebecca work?"""
    # Define the total number of hours worked by all three people
    total_hours = 157

    # Define the number of hours worked by Thomas
    thomas_hours = x

    # Define the number of hours worked by Toby (in terms of Thomas's hours)
    toby_hours = 2 * thomas_hours - 10

    # Define the number of hours worked by Rebecca (in terms of Toby's hours)
    rebecca_hours = toby_hours - 8

    # Calculate the total number of hours worked by all three people
    total_worked = thomas_hours + toby_hours + rebecca_hours

    # Solve for x by setting the total hours worked equal to the given total
    x = (total_hours - toby_hours - rebecca_hours) / 1

    # Return the hours worked by Rebecca
    result = rebecca_hours
    return result

print(solution())