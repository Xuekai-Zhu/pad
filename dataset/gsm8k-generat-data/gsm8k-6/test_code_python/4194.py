def solution():
    # Calculate the total number of apples in 3 boxes
    total_apples = 14 * 3

    # Calculate the number of days both brothers can eat the apples
    days = total_apples / 2  # each brother eats one apple per day

    # Calculate the number of weeks both brothers can eat the apples
    weeks = days / 7

    result = weeks
    return result

print(solution())