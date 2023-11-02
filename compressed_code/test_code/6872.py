def solution():
    
    susy_start_followers = 100
    sarah_start_followers = 50
    
    
    susy_new_followers_week1 = 40
    susy_new_followers_week2 = susy_new_followers_week1 / 2
    susy_new_followers_week3 = susy_new_followers_week2 / 2
    
    susy_total_followers = susy_start_followers + susy_new_followers_week1 + susy_new_followers_week2 + susy_new_followers_week3
    
    
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