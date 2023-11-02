def solution():
    """Maurice is getting $2 for every finished task. And for every 10 tasks finished, he receives a $6 bonus. How much money would Maurice make for finishing 30 tasks?"""
    tasks = 30
    task_pay = 2
    bonus = 6
    tasks_per_bonus = 10
    full_bonuses = tasks // tasks_per_bonus
    remaining_tasks = tasks % tasks_per_bonus
    total_pay = (full_bonuses * bonus) + (remaining_tasks * task_pay)
    result = total_pay
    return result

print(solution())