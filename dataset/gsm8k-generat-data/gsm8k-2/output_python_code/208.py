def solution():
    """John puts $25 in his piggy bank every month for 2 years to save up for a vacation. He had to spend $400 from his piggy bank savings last week to repair his car. How many dollars are left in his piggy bank?"""
    total_months = 24
    monthly_savings = 25
    total_savings = total_months * monthly_savings
    car_repair_cost = 400
    remaining_savings = total_savings - car_repair_cost
    result = remaining_savings
    return result

print(solution())