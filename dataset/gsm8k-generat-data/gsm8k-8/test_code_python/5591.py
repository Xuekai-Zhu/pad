def solution():
    current_time = 30 # initial time on day 3
    increment = 10 # amount of time added each day
    days = 3 # number of days so far
    
    while current_time < 90:
        current_time += increment # add 10 seconds to current time
        increment += 10 # increase the amount of time added each day
        days += 1 # increment the number of days

    result = days
    return result

print(solution())