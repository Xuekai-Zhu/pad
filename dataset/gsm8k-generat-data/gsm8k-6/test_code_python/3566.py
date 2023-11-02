def solution():
    # Calculate the number of students who bring their lunch
    cafeteria_students = 10
    lunch_bringers = cafeteria_students * 3

    # Calculate the number of students who don't eat lunch
    total_students = 60
    no_lunch = total_students - (cafeteria_students + lunch_bringers)

    result = no_lunch
    return result

print(solution())