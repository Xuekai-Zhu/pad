def solution():
    
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