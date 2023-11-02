def solution():
    """Jason worked for 9 years as a bartender and 3 years and six months as a manager. How many months of work experience does he have total?"""
    bartender_years = 9
    manager_years = 3.5
    total_years = bartender_years + manager_years
    total_months = total_years * 12
    result = total_months
    return result

print(solution())