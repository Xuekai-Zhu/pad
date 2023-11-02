def solution():
    total_students = 500  # There are 500 students in the high school
    juniors_percentage = 0.4  # 40% of students are juniors
    juniors_total = total_students * juniors_percentage  # Calculate the total number of juniors
    juniors_sports_percentage = 0.7  # 70% of juniors are involved in sports

    # Calculate the number of juniors involved in sports
    juniors_in_sports = juniors_total * juniors_sports_percentage
    result = juniors_in_sports
    return result

print(solution())