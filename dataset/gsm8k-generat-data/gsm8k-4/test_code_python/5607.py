def solution():
    """Johnny spent 3 hours working on a job that paid $7 per hour, 2 hours working on a job that paid $10 an hour, and 4 hours working on a job that paid $12 an hour. Assuming he repeats this process 5 days in a row, how much does Johnny make?"""
    # Define the hourly rates and hours worked for each job
    job1_rate = 7
    job1_hours = 3
    job2_rate = 10
    job2_hours = 2
    job3_rate = 12
    job3_hours = 4

    # Calculate the total earnings for each day
    daily_earnings = (job1_rate * job1_hours) + (job2_rate * job2_hours) + (job3_rate * job3_hours)

    # Calculate the total earnings for 5 days
    total_earnings = daily_earnings * 5

    result = total_earnings
    return result

print(solution())