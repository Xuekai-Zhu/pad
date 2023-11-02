def solution():
    # Calculate the total amount of rain on Mondays and Tuesdays respectively
    rain_on_mondays = 7 * 1.5  # 7 Mondays with 1.5cm each
    rain_on_tuesdays = 9 * 2.5  # 9 Tuesdays with 2.5cm each

    # Calculate the difference in rainfall between Tuesdays and Mondays
    difference = rain_on_tuesdays - rain_on_mondays
    result = difference
    return result

print(solution())