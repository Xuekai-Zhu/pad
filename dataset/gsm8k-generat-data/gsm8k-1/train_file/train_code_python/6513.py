def solution():
    """There are 500 students in a local high school. 40 percent are juniors. 70 percent of juniors are involved in sports. How many juniors are involved in sports?"""
    total_students = 500
    junior_percent = 40
    juniors = (total_students * junior_percent) / 100
    sports_percent = 70
    juniors_in_sports = (juniors * sports_percent) / 100
    result = juniors_in_sports
    return result

print(solution())