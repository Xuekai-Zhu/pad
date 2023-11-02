def solution():
    """A Statistics student wants to find out the average daily allowance of the middle school students. According to his survey, 2/3 of the students receive an average of $6 allowance per day while the rest gets an average of $4 a day. If he surveyed 60 students, what is the total amount of money those 60 students get in a day?"""
    surveyed_students = 60
    two_thirds_students = (2/3) * surveyed_students
    one_third_students = surveyed_students - two_thirds_students
    average_allowance_two_thirds = 6
    average_allowance_one_third = 4
    total_money = (two_thirds_students * average_allowance_two_thirds) + (one_third_students * average_allowance_one_third)
    result = total_money

    return result

print(solution())