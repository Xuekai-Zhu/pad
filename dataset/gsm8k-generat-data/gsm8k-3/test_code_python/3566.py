def solution():
    """A class has 60 students. The number of students who bring their lunch is thrice the number of those who eat in the school cafeteria. The rest of the students don't eat lunch. If 10 students eat in the school cafeteria, how many don't eat lunch?"""
    # Define the total number of students
    total_students = 60

    # Calculate the number of students who bring their lunch
    lunch_bringers = 3 * 10

    # Calculate the number of students who eat in the school cafeteria
    cafeteria_eaters = 10

    # Calculate the number of students who don't eat lunch
    non_eaters = total_students - (lunch_bringers + cafeteria_eaters)

    # Display the number of students who don't eat lunch
    result = non_eaters
    return result

print(solution())