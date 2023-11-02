def solution():
    """Linda makes $10.00 an hour babysitting.  There is a $25.00 application fee for each college application she submits.  If she is applying to 6 colleges, how many hours will she need to babysit to cover the application fees?"""
    # Define the hourly wage and application fee
    HOURLY_WAGE = 10
    APPLICATION_FEE = 25

    # Define the number of colleges Linda is applying to
    num_colleges = 6

    # Calculate the total cost of the application fees
    total_cost = num_colleges * APPLICATION_FEE

    # Calculate the number of hours Linda needs to babysit to cover the application fees
    hours_needed = total_cost / HOURLY_WAGE

    # Display the number of hours needed
    result = hours_needed
    return result

print(solution())