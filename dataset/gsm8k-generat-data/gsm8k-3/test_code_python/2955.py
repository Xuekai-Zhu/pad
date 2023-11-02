def solution():
    """Mo is buying valentine's day cards for the class. There are 30 students and he wants to give a Valentine to 60% of them. They cost $2 each. If he has $40, what percentage of his money will he spend on Valentine?"""
    # Define the number of students and the percentage receiving valentines
    student_count = 30
    valentine_percentage = 0.6

    # Calculate the number of students receiving valentines
    valentine_count = student_count * valentine_percentage

    # Calculate the total cost of the valentines
    valentine_cost = valentine_count * 2

    # Calculate the percentage of Mo's money spent on valentines
    percent_spent = (valentine_cost / 40) * 100

    # Display the percentage of money spent
    result = percent_spent
    return result

print(solution())