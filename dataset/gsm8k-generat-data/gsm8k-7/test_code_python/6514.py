def solution():
    total_students = 500
    junior_percentage = 0.4
    sports_percentage = 0.7

    # Calculate the number of juniors
    num_juniors = total_students * junior_percentage

    # Calculate the number of juniors involved in sports
    num_juniors_sports = num_juniors * sports_percentage
    result = num_juniors_sports
    return result

print(solution())