def solution():
    """Annabelle is saving for a phone that costs $400. She already has $80 in her savings. Her first job, where she earns $10 per hour, pays her for 20 hours of work. She is also paid for 15 hours of work at her second job, where she earns $5 an hour. In dollars, how much money does Annabelle still need to save?"""
    phone_cost = 400
    current_savings = 80
    job1_pay_rate = 10
    job1_hours = 20
    job2_pay_rate = 5
    job2_hours = 15
    
    job1_pay = job1_pay_rate * job1_hours
    job2_pay = job2_pay_rate * job2_hours
    
    total_income = job1_pay + job2_pay + current_savings
    remaining_cost = phone_cost - total_income
    
    result = remaining_cost
    return result

print(solution())