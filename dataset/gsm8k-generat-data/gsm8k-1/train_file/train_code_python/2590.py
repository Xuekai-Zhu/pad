def solution():
    """In one week, Jake can eat 3 papayas, his brother can eat 5 papayas, and his father can eat 4 papayas. To account for 4 weeks, how many papayas does Jake need to buy from the farmer’s market?"""
    papayas_per_week = 3 + 5 + 4
    weeks = 4
    total_papayas_needed = papayas_per_week * weeks
    result = total_papayas_needed
    return result

print(solution())