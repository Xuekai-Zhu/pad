def solution():
    # Calculate the total number of pills Antonia has to work with
    total_pills = 3*120 + 2*30  # 3 bottles of 120 pills each, 2 bottles of 30 pills each
    
    # Calculate the number of pills Antonia needs for 2 weeks
    pills_per_week = 7*5  # Antonia needs one pill of each supplement per day, for a total of 5 pills per day, so she needs 35 pills per week
    pills_for_two_weeks = 2*pills_per_week
    
    # Calculate the number of pills Antonia has left after filling her pillbox for 2 weeks
    pills_left = total_pills - pills_for_two_weeks
    result = pills_left
    return result

print(solution())