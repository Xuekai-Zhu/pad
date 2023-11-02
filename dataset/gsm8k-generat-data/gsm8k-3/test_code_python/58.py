def solution():
    """A Statistics student wants to find out the average daily allowance of the middle school students. According to his survey, 2/3 of the students receive an average of $6 allowance per day while the rest gets an average of $4 a day. If he surveyed 60 students, what is the total amount of money those 60 students get in a day?"""
    # Define the number of students receiving $6 allowance and the number of students receiving $4 allowance
    six_allowance_students = (2/3) * 60
    four_allowance_students = 60 - six_allowance_students

    # Calculate the total amount of money the students receiving $6 allowance get
    six_allowance_money = six_allowance_students * 6

    # Calculate the total amount of money the students receiving $4 allowance get
    four_allowance_money = four_allowance_students * 4

    # Calculate the total amount of money all the students get
    total_money = six_allowance_money + four_allowance_money

    # return the result
    result = total_money
    return result

print(solution())