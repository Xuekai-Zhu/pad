def solution():
    total_students = 25  # There are 25 students in the class
    fry_lovers = 15  # 15 students like French fries
    burger_lovers = 10  # 10 students like burgers
    both_lovers = 6  # 6 students like both French fries and burgers

    # Calculate the number of students who like only French fries
    fry_only = fry_lovers - both_lovers

    # Calculate the number of students who like only burgers
    burger_only = burger_lovers - both_lovers

    # Calculate the number of students who don't like either food
    neither = total_students - (fry_only + burger_only + both_lovers)
    result = neither
    return result

print(solution())