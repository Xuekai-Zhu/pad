def solution():
    """Mo is buying valentine's day cards for the class. There are 30 students and he wants to give a Valentine to 60% of them. They cost $2 each. If he has $40, what percentage of his money will he spend on Valentine?"""
    # Define the total number of students and the percentage of students receiving a Valentine
    total_students = 30
    valentine_percentage = 0.6

    # Calculate the number of students receiving a Valentine
    valentine_students = total_students * valentine_percentage

    # Calculate the total cost of the Valentines
    valentine_cost = valentine_students * 2

    # Calculate the percentage of Mo's money spent on Valentines
    money_percentage = (valentine_cost / 40) * 100

    # Return the result
    result = money_percentage
    return result

print(solution())