def solution():
    """Johnny spent 3 hours working on a job that paid $7 per hour, 2 hours working on a job that paid $10 an hour, and 4 hours working on a job that paid $12 an hour.  Assuming he repeats this process 5 days in a row, how much does Johnny make?"""
    # Define the pay rate for each job
    JOB1_RATE = 7
    JOB2_RATE = 10
    JOB3_RATE = 12

    # Define the number of hours worked for each job
    job1_hours = 3
    job2_hours = 2
    job3_hours = 4

    # Calculate the total earnings for each day
    day1_earnings = (job1_hours * JOB1_RATE) + (job2_hours * JOB2_RATE) + (job3_hours * JOB3_RATE)
    day2_earnings = (job1_hours * JOB1_RATE) + (job2_hours * JOB2_RATE) + (job3_hours * JOB3_RATE)
    day3_earnings = (job1_hours * JOB1_RATE) + (job2_hours * JOB2_RATE) + (job3_hours * JOB3_RATE)
    day4_earnings = (job1_hours * JOB1_RATE) + (job2_hours * JOB2_RATE) + (job3_hours * JOB3_RATE)
    day5_earnings = (job1_hours * JOB1_RATE) + (job2_hours * JOB2_RATE) + (job3_hours * JOB3_RATE)

    # Calculate the total earnings over 5 days
    total_earnings = day1_earnings + day2_earnings + day3_earnings + day4_earnings + day5_earnings

    # Display the total earnings
    result = total_earnings
    return result

print(solution())