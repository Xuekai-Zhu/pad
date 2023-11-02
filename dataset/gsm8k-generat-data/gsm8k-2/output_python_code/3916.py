def solution():
    """When Jack traveled to Canada, he had to wait 20 hours to get through customs, plus 14 days in coronavirus quarantine. How many hours total did Jack have to wait?"""
    customs_wait = 20
    quarantine_days = 14
    quarantine_wait = quarantine_days * 24
    total_wait = customs_wait + quarantine_wait
    result = total_wait
    return result

print(solution())