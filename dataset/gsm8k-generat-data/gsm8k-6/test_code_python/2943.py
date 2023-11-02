def solution():
    # Calculate the final temperature
    initial_temp = 40
    jerry_temp = initial_temp * 2
    dad_temp = jerry_temp - 30
    mom_temp = dad_temp * 0.7
    sister_temp = mom_temp + 24
    result = sister_temp
    return result

print(solution())