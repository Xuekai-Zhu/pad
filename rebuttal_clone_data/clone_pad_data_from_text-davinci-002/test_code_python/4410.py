def solution():
    rows_of_corn = 5
    stalks_per_row = 80
    bushels_per_eight_stalks = 1
    total_bushels = rows_of_corn * stalks_per_row / bushels_per_eight_stalks
    result = total_bushels
    return result

print(solution())