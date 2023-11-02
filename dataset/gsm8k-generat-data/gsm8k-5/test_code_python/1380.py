def solution():
    # Calculate Susy's total number of social media followers after 3 weeks
    susy_start = 100
    susy_week1 = 40
    susy_week2 = susy_week1 / 2
    susy_week3 = susy_week2 / 2
    susy_total_followers = susy_start + susy_week1 + susy_week2 + susy_week3

    # Calculate Sarah's total number of social media followers after 3 weeks
    sarah_start = 50
    sarah_week1 = 90
    sarah_week2 = sarah_week1 / 3
    sarah_week3 = sarah_week2 / 3
    sarah_total_followers = sarah_start + sarah_week1 + sarah_week2 + sarah_week3

    # Determine who has the most total followers
    if susy_total_followers > sarah_total_followers:
        result = susy_total_followers
    else:
        result = sarah_total_followers
    return result

print(solution())