def solution():
    forms_per_clerk = 25
    total_forms = 2400
    hours_worked = 8
    total_clerks_needed = total_forms / (forms_per_clerk * hours_worked)
    result = total_clerks_needed
    return result

print(solution())