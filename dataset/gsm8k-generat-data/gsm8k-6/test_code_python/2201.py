def solution():
    # Calculate the total number of roses planted by Uncle Welly
    roses_day1 = 50  # roses planted two days ago
    roses_day2 = roses_day1 + 20  # roses planted yesterday
    roses_day3 = 2 * roses_day1  # roses planted today
    total_roses = roses_day1 + roses_day2 + roses_day3  # total number of roses planted
    result = total_roses
    return result

print(solution())