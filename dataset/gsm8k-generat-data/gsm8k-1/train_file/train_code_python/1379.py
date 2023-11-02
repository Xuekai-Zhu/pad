def solution():
    """Susy goes to a large school with 800 students, while Sarah goes to a smaller school with only 300 students. At the start of the school year, Susy had 100 social media followers. She gained 40 new followers in the first week of the school year, half that in the second week, and half of that in the third week. Sarah only had 50 social media followers at the start of the year, but she gained 90 new followers the first week, a third of that in the second week, and a third of that in the third week. After three weeks, how many social media followers did the girl with the most total followers have?"""
    susy_start_followers = 100
    sarah_start_followers = 50
    
    # Susy's new followers
    susy_new_followers_week1 = 40
    susy_new_followers_week2 = susy_new_followers_week1 / 2
    susy_new_followers_week3 = susy_new_followers_week2 / 2
    
    susy_total_followers = susy_start_followers + susy_new_followers_week1 + susy_new_followers_week2 + susy_new_followers_week3
    
    # Sarah's new followers
    sarah_new_followers_week1 = 90
    sarah_new_followers_week2 = sarah_new_followers_week1 / 3
    sarah_new_followers_week3 = sarah_new_followers_week2 / 3
    
    sarah_total_followers = sarah_start_followers + sarah_new_followers_week1 + sarah_new_followers_week2 + sarah_new_followers_week3
    
    if susy_total_followers >= sarah_total_followers:
        result = susy_total_followers
    else:
        result = sarah_total_followers
    
    return result

print(solution())