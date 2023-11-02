def solution():
    """A Statistics student wants to find out the average daily allowance of the middle school students. According to his survey, 2/3 of the students receive an average of $6 allowance per day while the rest gets an average of $4 a day. If he surveyed 60 students, what is the total amount of money those 60 students get in a day?"""
    # Define the total number of students surveyed
    total_students = 60

    # Calculate the number of students who receive $6 allowance per day
    six_dollar_students = total_students * (2/3)

    # Calculate the number of students who receive $4 allowance per day
    four_dollar_students = total_students - six_dollar_students

    # Calculate the total amount of money received by the students per day
    total_money = (six_dollar_students * 6) + (four_dollar_students * 4)

    # return the result
    result = total_money
    return result

print(solution())