def solution():
    # Define the fat content of one hamburger and the recommended daily allowance
    hamburger_fat = 10
    daily_fat_min = 44
    daily_fat_max = 77
    # Calculate the fat content of seven hamburgers
    total_fat = hamburger_fat * 7
    # Check if the total fat exceeds the recommended daily allowance
    if total_fat > daily_fat_max:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())