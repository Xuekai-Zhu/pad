def solution():
    # Calculate the total tips made by Wade over 3 days
    friday_tips = 2 * 28  
    saturday_tips = 2 * 3 * 28  # Wade served three times as many customers on Saturday as on Friday
    sunday_tips = 2 * 36  
    total_tips = friday_tips + saturday_tips + sunday_tips

    result = total_tips
    return result

print(solution())