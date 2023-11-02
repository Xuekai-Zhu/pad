def solution():
    # Define the number of students who eat in the cafeteria
    cafeteria_students = 10

    # Calculate the number of students who bring lunch
    lunch_students = cafeteria_students * 3

    # Calculate the total number of students who eat lunch
    total_lunch_students = cafeteria_students + lunch_students

    # Calculate the number of students who don't eat lunch
    no_lunch_students = 60 - total_lunch_students
    result = no_lunch_students
    return result

print(solution())