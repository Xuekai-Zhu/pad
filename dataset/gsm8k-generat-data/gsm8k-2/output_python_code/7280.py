def solution():
    """Sean played cricket for 50 minutes each day for 14 days. Indira also played cricket. Together they played cricket for 1512 minutes. How many minutes did Indira play cricket?"""
    sean_minutes = 50 * 14
    indira_minutes = 1512 - sean_minutes
    result = indira_minutes
    return result

print(solution())