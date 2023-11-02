def solution():
    # Calculate the total tips Jerry has earned in the past 4 nights
    past_tips_total = 20 + 60 + 15 + 40

    # Calculate the total tips Jerry wants to earn in 5 nights to achieve an average of $50 per night
    target_tips_total = 5 * 50

    # Calculate how much Jerry needs to earn tonight to reach his target tips total
    tonight_tips_needed = target_tips_total - past_tips_total

    result = tonight_tips_needed
    return result

print(solution())