Sorry, I cannot provide a solution to the Samantha's last name problem as there are missing information and context that is needed in order to solve it. As for the James hires a horse-drawn carriage problem, here's the solution:

def solution():
    """James hires a horse-drawn carriage from 5 PM to 9 PM. He gets 1 hour free. The first paid hour is $15 and each hour after that is twice the cost. How much did he pay?"""
    first_hour_cost = 15
    additional_hour_cost = first_hour_cost * 2
    total_hours = 4
    free_hours = 1
    paid_hours = total_hours - free_hours
    total_cost = first_hour_cost + (additional_hour_cost * (paid_hours-1))
    result = total_cost
    
    return result

print(solution())