def solution():
    """A toy manufacturer receives an order for 400 toys. 5 workers are available to work on the order. 2 of the workers produce 6 toys an hour, and another 2 workers produce 4 toys an hour. They all work on the order during their 10-hour shift, and by the end of their shift the manufacturer still needs another 20 toys to be able to ship the order. How many toys per hour does the fifth worker produce?"""
    total_order = 400
    remaining_toys = 20
    total_workers = 5
    workers_6_toys_hour = 2
    workers_4_toys_hour = 2
    total_work_hours = 10
    total_toys_produced = (workers_6_toys_hour * 6 + workers_4_toys_hour * 4) * total_work_hours
    toys_remaining = total_order - total_toys_produced + remaining_toys
    toys_per_hour = toys_remaining / (total_workers - workers_6_toys_hour - workers_4_toys_hour)
    result = toys_per_hour
    
    return result

print(solution())