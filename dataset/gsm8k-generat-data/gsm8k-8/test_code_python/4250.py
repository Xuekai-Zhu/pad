def solution():
    # Define the number of students helping
    num_students = 4

    # Define the number of chairs each student can carry per trip
    chairs_per_student = 5

    # Define the number of trips made by each student
    trips_per_student = 10

    # Calculate the total number of chairs
    total_chairs = num_students * chairs_per_student * trips_per_student
    result = total_chairs
    return result

print(solution())