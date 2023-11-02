def solution():
    sunday_rainfall = 4  # It rained 4 inches on Sunday
    monday_rainfall = sunday_rainfall + 3  # It rained 3 inches more on Monday than Sunday
    tuesday_rainfall = monday_rainfall * 2  # It rained twice as much on Tuesday as Monday

    # Calculate the total rainfall over 3 days
    total_rainfall = sunday_rainfall + monday_rainfall + tuesday_rainfall
    result = total_rainfall
    return result

print(solution())