def solution():
    rainfall_mon = 1
    hours_mon = 7
    rainfall_tue = 2
    hours_tue = 4
    rainfall_wed = 4
    hours_wed = 2
    total_rainfall = (rainfall_mon * hours_mon) + (rainfall_tue * hours_tue) + (rainfall_wed * hours_wed)
    result = total_rainfall
    return result

print(solution())