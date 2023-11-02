def solution():
    """Johnny spent 3 hours working on a job that paid $7 per hour, 2 hours working on a job that paid $10 an hour, and 4 hours working on a job that paid $12 an hour. Assuming he repeats this process 5 days in a row, how much does Johnny make?"""
    job1_hours = 3
    job1_pay = 7
    job2_hours = 2
    job2_pay = 10
    job3_hours = 4
    job3_pay = 12
    days_worked = 5
    total_pay = (job1_hours * job1_pay + job2_hours * job2_pay + job3_hours * job3_pay) * days_worked
    result = total_pay
    return result

print(solution())