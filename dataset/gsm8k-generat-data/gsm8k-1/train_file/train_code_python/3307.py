def solution():
    """Jason worked for 9 years as a bartender and 3 years and six months as a manager. How many months of work experience does he have total?"""
    months_worked_as_bartender = 9 * 12
    months_worked_as_manager = (3 * 12) + 6
    total_months_worked = months_worked_as_bartender + months_worked_as_manager
    result = total_months_worked
    return result

print(solution())