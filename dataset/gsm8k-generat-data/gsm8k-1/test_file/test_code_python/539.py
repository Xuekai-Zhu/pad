def solution():
    """For each small task accomplished, Jairus gets $0.8 while Jenny gets $0.5. If each of them finished 20 tasks, how much more will Jairus get than Jenny?"""
    jairus_pay = 0.8
    jenny_pay = 0.5
    num_tasks = 20
    jairus_total_pay = jairus_pay * num_tasks
    jenny_total_pay = jenny_pay * num_tasks
    difference = jairus_total_pay - jenny_total_pay
    result = difference
    
    return result

print(solution())