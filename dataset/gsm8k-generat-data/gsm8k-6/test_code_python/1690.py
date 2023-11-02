def solution():
    # Calculate the total rainfall on Mondays and Tuesdays
    total_Mondays = 7 * 1.5  # 1.5 centimeters of rain on each of 7 Mondays
    total_Tuesdays = 9 * 2.5  # 2.5 centimeters of rain on each of 9 Tuesdays
    difference = total_Tuesdays - total_Mondays  # calculate the difference between the two totals

    result = difference
    return result

print(solution())