def solution():
    # Calculate the total number of birds caught by the cat
    day_catch = 8  # number of birds caught during the day
    night_catch = 2 * day_catch  # number of birds caught at night
    total_catch = day_catch + night_catch  # total number of birds caught
    result = total_catch
    return result

print(solution())