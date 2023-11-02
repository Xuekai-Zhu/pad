def solution():
    
    customs_wait = 20
    quarantine_days = 14
    quarantine_wait = quarantine_days * 24
    total_wait = customs_wait + quarantine_wait
    result = total_wait
    return result

print(solution())