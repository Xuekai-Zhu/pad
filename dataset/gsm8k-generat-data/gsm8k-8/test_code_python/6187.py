def solution():
    # Calculate the percent decrease
    percent_decrease = 2/100

    # Calculate the value of the Dow before the decrease
    dow_before_decrease = 8722 / (1 - percent_decrease)

    # Round the result to the nearest whole number
    dow_before_decrease = round(dow_before_decrease)

    result = dow_before_decrease
    return result

print(solution())