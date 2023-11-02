def solution():
    marios_salary = 4000
    bob_salary_last_year = 3 * marios_salary
    bob_salary_increase = 0.2  # 20% increase
    bob_salary_current = bob_salary_last_year * (1 + bob_salary_increase)
    result = bob_salary_current
    return result

print(solution())