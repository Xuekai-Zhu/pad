def solution():
    """To try to get the class to eat more vegetables, the teacher says that she will start giving them good character points that the class can redeem for a movie day if they earn enough. The students need to earn 200 points to win the movie day. Each time a student eats their vegetables at lunch she gives the student 2 points. There are 25 students in the class. If they have two school weeks, otherwise known as 10 days to win the movie, what is the average number of vegetables each student must eat per school week to get a movie day?"""
    # Define the number of points per vegetable eaten
    POINTS_PER_VEGETABLE = 2

    # Define the number of students in the class
    num_students = 25

    # Define the number of days the class has to earn 200 points
    num_days = 10

    # Calculate the total number of points the class needs to earn
    total_points_needed = 200

    # Calculate the total number of points the class can earn in one day if every student eats their vegetables
    total_points_per_day = num_students * POINTS_PER_VEGETABLE

    # Calculate the total number of points the class can earn in two weeks
    total_points_two_weeks = total_points_per_day * num_days

    # Calculate the average number of vegetables each student must eat per school week to get a movie day
    avg_vegetables_per_week = (total_points_needed / total_points_per_day) / 2

    # Display the average number of vegetables each student must eat per school week
    result = avg_vegetables_per_week
    return result

print(solution())