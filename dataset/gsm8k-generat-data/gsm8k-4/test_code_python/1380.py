def solution():
    """Susy goes to a large school with 800 students, while Sarah goes to a smaller school with only 300 students. At the start of the school year, Susy had 100 social media followers. She gained 40 new followers in the first week of the school year, half that in the second week, and half of that in the third week. Sarah only had 50 social media followers at the start of the year, but she gained 90 new followers the first week, a third of that in the second week, and a third of that in the third week. After three weeks, how many social media followers did the girl with the most total followers have?"""
    
    # Calculate Susy's total number of social media followers after three weeks
    susy_followers = 100 + 40 + 20 + 10
    
    # Calculate Sarah's total number of social media followers after three weeks
    sarah_followers = 50 + 90/3 + 30/3
    
    # Determine which girl has more followers and return the result
    if susy_followers > sarah_followers:
        result = susy_followers
    else:
        result = sarah_followers
    return result

print(solution())