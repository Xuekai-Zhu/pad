def solution():
    # Calculate the total tips Jerry has earned in the past 4 nights
    total_tips = 20 + 60 + 15 + 40
    
    # Calculate the amount of tips Jerry needs to earn tonight
    needed_tips = (5 * 50) - total_tips  # Jerry wants to make an average of $50 in tips per night over 5 days
    
    result = needed_tips
    return result

print(solution())