def solution():
    
    total_budget = 32
    policing_budget = total_budget / 2
    education_budget = 12
    public_spaces_budget = total_budget - policing_budget - education_budget
    result = public_spaces_budget
    return result

print(solution())