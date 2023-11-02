def solution():
    """Thomas, Toby, and Rebecca worked a total of 157 hours in one week.  Thomas worked x hours.  Toby worked 10 hours less than twice what Thomas worked, and Rebecca worked 8 hours less than Toby.  How many hours did Rebecca work?"""
    # Get the number of hours Thomas worked
    x = int(input("Enter the number of hours Thomas worked: "))

    # Calculate the number of hours Toby worked
    toby_hours = 2*x - 10

    # Calculate the number of hours Rebecca worked
    rebecca_hours = toby_hours - 8

    # Calculate the total number of hours worked
    total_hours = x + toby_hours + rebecca_hours

    # Display the number of hours Rebecca worked
    result = rebecca_hours
    return result

print(solution())