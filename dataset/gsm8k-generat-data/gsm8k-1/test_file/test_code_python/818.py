def solution():
    """John does 30 cycles of work a day. Each cycle has 5 different tasks and each task pays $1.20. How much does he make if he works a full 7 day week?"""
    cycles_per_day = 30
    tasks_per_cycle = 5
    pay_per_task = 1.20
    days_per_week = 7
    total_tasks = cycles_per_day * tasks_per_cycle
    total_pay = total_tasks * pay_per_task * days_per_week
    result = total_pay
    return result

print(solution())