def solution():
    jake_papayas_per_week = 3
    brother_papayas_per_week = 5
    father_papayas_per_week = 4
    num_weeks = 4

    # Calculate the total number of papayas needed for one week
    total_papayas_per_week = jake_papayas_per_week + brother_papayas_per_week + father_papayas_per_week

    # Calculate the total number of papayas needed for all 4 weeks
    total_papayas = total_papayas_per_week * num_weeks
    result = total_papayas
    return result

print(solution())