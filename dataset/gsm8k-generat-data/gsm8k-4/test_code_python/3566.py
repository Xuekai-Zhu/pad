def solution():
    """A class has 60 students. The number of students who bring their lunch is thrice the number of those who eat in the school cafeteria. The rest of the students don't eat lunch. If 10 students eat in the school cafeteria, how many don't eat lunch?"""
    # Define the total number of students
    total_students = 60

    # Define the number of students who eat in the cafeteria
    cafeteria_students = 10

    # Calculate the number of students who bring their lunch
    lunchbox_students = cafeteria_students * 3

    # Calculate the number of students who don't eat lunch
    no_lunch_students = total_students - cafeteria_students - lunchbox_students

    # return the result
    result = no_lunch_students
    return result

print(solution())