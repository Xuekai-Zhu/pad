def solution():
    # Calculate the initially bought diaries
    initially_bought = 8 * 2

    # Calculate the number of diaries lost
    lost_diaries = initially_bought * 0.25

    # Calculate the current number of diaries
    current_diaries = initially_bought - lost_diaries
    result = current_diaries
    return result

print(solution())