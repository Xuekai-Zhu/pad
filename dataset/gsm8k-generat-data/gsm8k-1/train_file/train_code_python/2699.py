def solution():
    """To try to get the class to eat more vegetables, the teacher says that she will start giving them good character points that the class can redeem for a movie day if they earn enough.
    The students need to earn 200 points to win the movie day. Each time a student eats their vegetables at lunch she gives the student 2 points.
    There are 25 students in the class. If they have two school weeks, otherwise known as 10 days to win the movie,
    what is the average number of vegetables each student must eat per school week to get a movie day?"""
    
    required_points = 200
    points_per_veggie = 2
    num_students = 25
    num_days = 10
    total_points = num_students * points_per_veggie * num_days
    avg_veggies_per_week = (required_points / total_points) * (num_days / 5) * num_students
    
    result = avg_veggies_per_week
    
    return result

print(solution())