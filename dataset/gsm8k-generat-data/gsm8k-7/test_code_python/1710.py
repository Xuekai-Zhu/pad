def solution():
    temperatures = [90, 90, 90, 79, 71]
    num_years = len(temperatures)

    # Calculate the total temperature over the past 5 years
    total_temp = sum(temperatures)

    # Calculate the average temperature
    avg_temp = total_temp / num_years
    result = avg_temp
    return result

print(solution())