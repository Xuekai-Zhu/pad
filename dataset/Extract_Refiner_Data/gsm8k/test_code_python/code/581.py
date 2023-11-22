def solution():
    
    # Define the hourly rate and the number of hours worked
    hourly_rate = 10
    saturday_hours = 2
    sunday_hours = 1

    # Calculate the total hours worked by Jill and John
    jill_hours = saturday_hours + sunday_hours
    john_hours = jill_hours * 2 + saturday_hours * 3

    # Calculate the total earnings of Jill and John
    jill_earnings = jill_hours * hourly_rate
    john_earnings = john_hours * hourly_rate

    # Calculate the difference in earnings between John and Jill
    difference = john_earnings - jill_earnings

    # return the result
    result = difference
    return result

print(solution())