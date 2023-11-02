def solution():
    # Calculate Susy's total number of social media followers after 3 weeks
    susy_followers = 100 + 40 + 20 + 10  # gained 40 new followers in the first week, half that in the second week, and half of that in the third week

    # Calculate Sarah's total number of social media followers after 3 weeks
    sarah_followers = 50 + 90 + 30 + 10  # gained 90 new followers in the first week, a third of that in the second week, and a third of that in the third week

    # Determine which girl has the most total followers
    if susy_followers > sarah_followers:
        result = susy_followers
    else:
        result = sarah_followers
    return result

print(solution())