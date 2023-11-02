def solution():
    """Mr Fletcher hired 2 men to dig a well in his compound. They worked for 10 hours on the first day, 8 hours on the second day and finished the job on the third day after working 15 hours. If Mr Fletcher paid each of them $10 per hour of work, calculate the total amount of money they received altogether?"""
    # Define the hourly rate of pay
    hourly_rate = 10

    # Calculate the total number of hours worked by each worker
    worker1_hours = 10 + 8 + 5  # 5 hours of work on the third day
    worker2_hours = 10 + 8 + 5  # 5 hours of work on the third day

    # Calculate the total amount of money earned by each worker
    worker1_earnings = worker1_hours * hourly_rate
    worker2_earnings = worker2_hours * hourly_rate

    # Calculate the total amount of money earned by both workers together
    total_earnings = worker1_earnings + worker2_earnings

    # return the result
    result = total_earnings
    return result

print(solution())