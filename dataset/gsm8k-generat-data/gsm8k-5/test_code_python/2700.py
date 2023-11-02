def solution():
    points_needed = 200  # The class needs to earn 200 points to win the movie day
    points_per_veggie = 2  # Each vegetable eaten earns the student 2 points
    num_students = 25  # There are 25 students in the class
    school_weeks = 2  # There are 2 school weeks (10 days) to win the movie

    # Calculate the total number of points the class can earn in 2 weeks
    total_points_possible = points_per_veggie * num_students * school_weeks * 5  # 5 lunch days in a week

    # Calculate the average number of veggies each student must eat per school week
    veggies_per_week = (points_needed / 2) / (num_students * school_weeks)
    result = veggies_per_week
    return result

print(solution())