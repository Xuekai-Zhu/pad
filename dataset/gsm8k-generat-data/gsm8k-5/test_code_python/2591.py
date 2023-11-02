def solution():
    jake_per_week = 3  # Jake can eat 3 papayas per week
    brother_per_week = 5  # Jake's brother can eat 5 papayas per week
    father_per_week = 4  # Jake's father can eat 4 papayas per week
    weeks = 4  # Jake wants to know how many papayas he needs to buy for 4 weeks

    # Calculate the total number of papayas needed for 4 weeks
    total_papayas = (jake_per_week + brother_per_week + father_per_week) * weeks
    result = total_papayas
    return result

print(solution())