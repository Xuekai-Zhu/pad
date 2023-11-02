def solution():
    # Define the total number of students
    total_students = 500

    # Calculate the number of juniors
    juniors = int(total_students * 0.4)

    # Calculate the number of juniors involved in sports
    juniors_in_sports = int(juniors * 0.7)
    result = juniors_in_sports
    return result

print(solution())