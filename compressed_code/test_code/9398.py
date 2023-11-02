def solution():
    
    first_exp = 3
    second_exp = first_exp + 2
    last_exp = second_exp * 2
    total_weeks = first_exp + second_exp + last_exp
    total_days = total_weeks * 7
    result = total_days
    return result

print(solution())