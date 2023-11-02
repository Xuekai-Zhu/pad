def solution():
    # Calculate the time it takes for Mary and Ann to slide down their respective hills
    time_Mary = 630 / 90  # time = distance / speed
    time_Ann = 800 / 40
    
    # Calculate the difference in time between Ann and Mary
    time_diff = time_Ann - time_Mary
    
    # Convert the time difference to minutes
    time_diff_minutes = time_diff * 60
    
    result = time_diff_minutes
    return result

print(solution())