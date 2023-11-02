def solution():
    """Linda makes $10.00 an hour babysitting. There is a $25.00 application fee for each college application she submits. If she is applying to 6 colleges, how many hours will she need to babysit to cover the application fees?"""
    # Define the hourly rate and the number of colleges
    HOURLY_RATE = 10
    NUM_COLLEGES = 6

    # Calculate the total application fees
    total_fees = NUM_COLLEGES * 25

    # Calculate the number of hours needed to cover the fees
    hours_needed = total_fees / HOURLY_RATE

    # return the result
    result = hours_needed
    return result

print(solution())