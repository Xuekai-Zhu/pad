def solution():
    # Calculate the total number of cans collected yesterday and today
    total_yesterday = 50 + 80  # Sarah: 50 cans; Lara: 80 cans (30 more than Sarah)
    total_today = 40 + 70  # Sarah: 40 cans; Lara: 70 cans

    # Calculate the difference between the total cans collected yesterday and today
    less_today = total_yesterday - total_today
    result = less_today
    return result

print(solution())