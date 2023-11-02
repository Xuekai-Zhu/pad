def solution():
    # Calculate the total time spent traveling in a day
    total_time = 5 + 20 + 5 + 20 + 5 + 5  # 5 minutes walking to bus station, 20 minutes on bus, 5 minutes walking from bus station to job, and back again in the evening
    # Calculate the total time spent traveling in a year
    total_time_year = total_time * 365  # assuming Bryan works every day
    # Convert minutes to hours
    total_time_year_hours = total_time_year / 60
    result = total_time_year_hours
    return result

print(solution())