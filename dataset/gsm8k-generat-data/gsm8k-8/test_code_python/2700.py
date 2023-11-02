def solution():
    # Calculate the total points needed to win the movie day
    points_needed = 200

    # Calculate the total number of students
    num_students = 25

    # Calculate the total number of days to win the movie
    num_days = 10

    # Calculate the total number of points that can be earned
    total_points = num_students * 2 * num_days

    # Calculate the average number of vegetables each student must eat per school week
    veggies_per_week = (points_needed / num_students / 2) / 2

    result = veggies_per_week
    return result

print(solution())