def solution():
    """To try to get the class to eat more vegetables, the teacher says that she will start giving them good character points that the class can redeem for a movie day if they earn enough. The students need to earn 200 points to win the movie day. Each time a student eats their vegetables at lunch she gives the student 2 points. There are 25 students in the class. If they have two school weeks, otherwise known as 10 days to win the movie, what is the average number of vegetables each student must eat per school week to get a movie day?"""
    # Define the number of students, points needed to win the movie, and number of school days
    num_students = 25
    points_needed = 200
    school_days = 10

    # Calculate the total number of points the class can earn
    total_points = num_students * 2 * school_days

    # Calculate the average number of vegetables each student must eat per school week to earn enough points for the movie day
    veggies_per_week = (points_needed / (num_students * 2)) / 2

    # return the result
    result = veggies_per_week
    return result

print(solution())