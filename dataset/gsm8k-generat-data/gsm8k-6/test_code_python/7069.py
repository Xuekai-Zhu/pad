def solution():
    # Calculate the total rainfall for the three days
    monday_rainfall = 7 * 1  # 7 hours at a rate of 1 inch per hour
    tuesday_rainfall = 4 * 2  # 4 hours at a rate of 2 inches per hour
    wednesday_rainfall = 2 * 2 * 2  # 2 hours at a rate of twice that of the previous day
    total_rainfall = monday_rainfall + tuesday_rainfall + wednesday_rainfall

    result = total_rainfall
    return result

print(solution())