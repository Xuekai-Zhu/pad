def solution():
    # Calculate the total number of pomelos shipped
    total_pomelos = 10 * 240 + 20 * 240  # 10 boxes shipped last week, 20 boxes shipped this week and there were 240 pomelos in each box
    dozens_pomelos = total_pomelos / 12  # convert to dozens by dividing by 12
    result = dozens_pomelos
    return result

print(solution())