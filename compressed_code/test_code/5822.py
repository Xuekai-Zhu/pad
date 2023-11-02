def solution():
    
    baseball_expenses = 100 * 4
    non_baseball_months = 12 - 4
    savings_needed = baseball_expenses / non_baseball_months
    chores_needed = savings_needed / 10
    result = chores_needed
    return result

print(solution())