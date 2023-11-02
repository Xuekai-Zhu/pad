def solution():
    """When Jack traveled to Canada, he had to wait 20 hours to get through customs, plus 14 days in coronavirus quarantine. How many hours total did Jack have to wait?"""
    hours_in_quarantine = 14 * 24
    hours_in_customs = 20
    total_wait_hours = hours_in_quarantine + hours_in_customs
    result = total_wait_hours
    return result

print(solution())