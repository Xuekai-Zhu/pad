def solution():
    # Calculate the total number of minutes in 2 hours
    total_minutes = 2 * 60  

    # Calculate the total number of goals scored by Xavier in 2 hours
    total_goals = (total_minutes / 15) * 2  # Xavier can score 2 goals on average in 15 minutes

    # Calculate the average number of goals scored by Xavier per hour
    avg_goals = total_goals / 2  # 2 hours in a match
    result = avg_goals
    return result

print(solution())