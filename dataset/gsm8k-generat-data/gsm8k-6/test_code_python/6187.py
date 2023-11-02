def solution():
    # Calculate the Dow before the markets opened
    current_dow = 8722
    percent_change = 2/100
    dow_before_open = current_dow / (1 - percent_change)
    result = dow_before_open
    return result

print(solution())