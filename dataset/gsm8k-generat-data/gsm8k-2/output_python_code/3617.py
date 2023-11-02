def solution():
    """Maurice is getting $2 for every finished task. And for every 10 tasks finished, he receives a $6 bonus. How much money would Maurice make for finishing 30 tasks?"""
    task_payment = 2
    bonus_payment = 6
    total_tasks = 30
    bonus_tasks = total_tasks // 10
    regular_tasks = total_tasks - bonus_tasks
    total_payment = (regular_tasks * task_payment) + (bonus_tasks * bonus_payment)
    result = total_payment
    return result

print(solution())