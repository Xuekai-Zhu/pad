def solution():
    
    cycles_per_day = 30
    tasks_per_cycle = 5
    cost_per_task = 1.20
    days_per_week = 7
    total_tasks = cycles_per_day * tasks_per_cycle * days_per_week
    total_earnings = total_tasks * cost_per_task
    result = total_earnings
    return result

print(solution())