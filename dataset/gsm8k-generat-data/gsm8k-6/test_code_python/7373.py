def solution():
    # Calculate the total minutes Hank spends reading in one week
    newspaper_reading = 5 * 30  # 5 days a week for 30 minutes
    novel_reading = 5 * 60  # 5 days a week for 1 hour
    weekend_reading = (2 * newspaper_reading) + (2 * novel_reading)  # double the reading time on weekends
    total_reading = newspaper_reading + novel_reading + weekend_reading
    result = total_reading
    return result

print(solution())