def solution():
    # Initialize variables
    sarah_cans_yesterday = 50
    lara_cans_yesterday = 30
    sarah_cans_today = 40
    lara_cans_today = 70
    
    # Calculate the difference in cans collected
    total_cans_yesterday = sarah_cans_yesterday + lara_cans_yesterday
    total_cans_today = sarah_cans_today + lara_cans_today
    difference = total_cans_today - total_cans_yesterday
    
    # Return the result
    return difference

print(solution())