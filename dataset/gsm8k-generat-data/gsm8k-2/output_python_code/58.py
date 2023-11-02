def solution():
    """A Statistics student wants to find out the average daily allowance of the middle school students. According to his survey, 2/3 of the students receive an average of $6 allowance per day while the rest gets an average of $4 a day. If he surveyed 60 students, what is the total amount of money those 60 students get in a day?"""
    total_students = 60
    two_thirds = int(2/3 * total_students)
    remaining_students = total_students - two_thirds
    allowance_1 = 6
    allowance_2 = 4
    total_allowance_1 = two_thirds * allowance_1
    total_allowance_2 = remaining_students * allowance_2
    total_allowance = total_allowance_1 + total_allowance_2
    result = total_allowance
    return result

print(solution())