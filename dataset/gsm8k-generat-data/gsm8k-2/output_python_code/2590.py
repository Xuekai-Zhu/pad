def solution():
    """In one week, Jake can eat 3 papayas, his brother can eat 5 papayas, and his father can eat 4 papayas. To account for 4 weeks, how many papayas does Jake need to buy from the farmer’s market?"""
    jake_papayas_per_week = 3
    brother_papayas_per_week = 5
    father_papayas_per_week = 4
    total_papayas_per_week = jake_papayas_per_week + brother_papayas_per_week + father_papayas_per_week
    total_weeks = 4
    total_papayas = total_papayas_per_week * total_weeks
    result = total_papayas
    return result

print(solution())