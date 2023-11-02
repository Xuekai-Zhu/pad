def solution():
    """It rained twice as much on Tuesday as Monday. On Monday it rained 3 inches more than Sunday. It rained 4 inches on Sunday. How much total rainfall was there over the 3 days?"""
    sunday_rain = 4
    monday_rain = sunday_rain + 3
    tuesday_rain = monday_rain * 2
    total_rainfall = sunday_rain + monday_rain + tuesday_rain
    result = total_rainfall
    return result

print(solution())