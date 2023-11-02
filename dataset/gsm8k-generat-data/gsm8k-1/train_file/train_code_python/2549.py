def solution():
    """Nancy earns $28 for working 4 hours. How many hours does she have to work to earn $70?"""
    rate = 28/4 # hourly rate
    target_pay = 70
    hours_needed = target_pay / rate
    result = hours_needed
    return result

print(solution())