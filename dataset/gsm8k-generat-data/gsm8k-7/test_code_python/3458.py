def solution():
    jake_total_newspapers = 234 * 4 # 4 weeks in a month
    miranda_total_newspapers = jake_total_newspapers * 2 # Miranda delivers twice as many
    difference = miranda_total_newspapers - (234*4) # subtract Jake's total newspapers from Miranda's
    result = difference
    return result

print(solution())