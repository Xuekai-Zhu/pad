def solution():
    # Calculate the number of points needed to win the movie day
    points_needed = 200

    # Calculate the total number of students in the class
    total_students = 25

    # Calculate the number of days they have to earn the points
    total_days = 10

    # Calculate the average vegetables per student per week
    average_veggies = (points_needed / (total_students * total_days)) * 7 * 2

    result = average_veggies
    return result

print(solution())