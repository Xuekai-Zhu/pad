def solution():
    sunday_rainfall = 4
    monday_rainfall = sunday_rainfall + 3
    tuesday_rainfall = monday_rainfall * 2

    # Calculate total rainfall over 3 days
    total_rainfall = sunday_rainfall + monday_rainfall + tuesday_rainfall
    result = total_rainfall
    return result

print(solution())