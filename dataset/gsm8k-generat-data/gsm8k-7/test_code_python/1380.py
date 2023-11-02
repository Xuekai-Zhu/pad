def solution():
    susy_start_followers = 100
    susy_week1_followers = 40
    susy_week2_followers = susy_week1_followers / 2
    susy_week3_followers = susy_week2_followers / 2
    susy_total_followers = susy_start_followers + susy_week1_followers + susy_week2_followers + susy_week3_followers

    sarah_start_followers = 50
    sarah_week1_followers = 90
    sarah_week2_followers = sarah_week1_followers / 3
    sarah_week3_followers = sarah_week2_followers / 3
    sarah_total_followers = sarah_start_followers + sarah_week1_followers + sarah_week2_followers + sarah_week3_followers

    if susy_total_followers > sarah_total_followers:
        result = susy_total_followers
    else:
        result = sarah_total_followers
    return result

print(solution())