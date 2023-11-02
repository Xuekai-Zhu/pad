def solution():
    # Calculate the total number of reports received on Monday and Tuesday
    total_monday_tues = 1907

    # Calculate the total number of reports received on Thursday and Friday
    total_thursday_friday = 2136

    # Calculate the total number of reports received on Wednesday
    total_wednesday = 5168 + total_monday_tues + total_thursday_friday
    result = total_wednesday
    return result

print(solution())