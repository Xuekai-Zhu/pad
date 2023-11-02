def solution():
    New_York_cases = 2000
    California_cases = New_York_cases / 2
    Texas_cases = California_cases + 400
    total_cases = New_York_cases + California_cases + Texas_cases
    result = total_cases
    return result

print(solution())