def solution():
    # Calculate the total hours Oliver worked out from Monday to Wednesday
    monday = 4
    tuesday = monday - 2  # next day for 2 hours less
    wednesday = 2 * monday  # twice as much as on Monday
    total_mw = monday + tuesday + wednesday

    # Calculate the hours worked out on Thursday
    thursday = 2 * (tuesday - 2)  # twice as much time as on Tuesday

    # Calculate the total hours Oliver worked out
    total_hours = total_mw + thursday
    result = total_hours
    return result

print(solution())