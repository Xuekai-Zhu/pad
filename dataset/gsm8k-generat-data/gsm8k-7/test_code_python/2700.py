def solution():
    good_character_points_needed = 200
    points_per_veggie = 2
    num_students = 25
    num_school_weeks = 2
    num_school_days = 10

    # Calculate the total number of good character points that the class needs to earn
    total_good_character_points_needed = good_character_points_needed * num_students

    # Calculate the total number of points that the class can earn in a school week
    total_points_per_week = points_per_veggie * num_students * num_school_days

    # Calculate the average number of vegetables each student must eat per school week to get a movie day
    veggies_per_week = total_good_character_points_needed / total_points_per_week / num_school_weeks
    result = veggies_per_week
    return result

print(solution())