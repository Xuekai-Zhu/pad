def solution():
    """Every 4 weeks, Helen hand washes her silk pillowcases. It takes 30 minutes to hand wash all of them. In 1 year, how much time does Helen spend hand washing her pillowcases?"""
    pillowcases_per_month = 4
    handwashing_time = 30
    months_per_year = 12
    total_handwashing_time = pillowcases_per_month * handwashing_time * months_per_year
    result = total_handwashing_time
    return result

print(solution())