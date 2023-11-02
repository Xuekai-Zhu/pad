def solution():
    """In a factory that employed 852 people, 25% more workers have just been hired. How many employees are there now in the factory?"""
    initial_employees = 852
    percent_increase = 25
    additional_employees = initial_employees * (percent_increase / 100)
    total_employees = initial_employees + additional_employees
    result = total_employees
    return result

print(solution())