def solution():
    """Adrien's total salary was 30 percent higher than Lylah's. Four years later, his salary had increased, and he was earning 40% more than what he was making four
    years ago. If Adrien's and Lylah's salary increased simultaneously, and Adrien earned $40000 four years ago, calculate the total salary the two were receiving four
    years later?"""
    adrien_starting_salary = 40000
    lylah_starting_salary = (adrien_starting_salary * 100) / 130
    adrien_current_salary = adrien_starting_salary * 1.4
    lylah_current_salary = lylah_starting_salary * 1.4
    total_salary = adrien_current_salary + lylah_current_salary
    result = total_salary
    return result

print(solution())