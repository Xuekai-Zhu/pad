def solution():
    """In a company of 50 employees, 20% of the employees are management. Out of this 20%, only 30% oversee the entire company. How many employees oversee the company?"""
    total_employees = 50
    management_percent = 20
    oversee_percent = 30
    management_num = total_employees * (management_percent / 100)
    oversee_num = management_num * (oversee_percent / 100)
    result = oversee_num
    return result

print(solution())