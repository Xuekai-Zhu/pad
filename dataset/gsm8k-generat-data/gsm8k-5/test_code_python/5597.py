def solution():
    # Convert 4:00 pm to 24-hour format
    leaving_time = 16 

    # Calculate the time it will take for Jasmine to complete all her tasks
    total_time = 0.5 + 0.5 + 0.17 + 0.33 + 1.5  # in hours

    # Calculate the time Jasmine will eat dinner
    dinner_time = leaving_time + total_time

    # Convert dinner time back to 12-hour format
    if dinner_time > 12:
        dinner_time = dinner_time - 12
        time_of_day = 'pm'
    else:
        time_of_day = 'am'

    result = str(int(dinner_time)) + ':' + str(int((dinner_time % 1) * 60)).zfill(2) + ' ' + time_of_day
    return result

print(solution())