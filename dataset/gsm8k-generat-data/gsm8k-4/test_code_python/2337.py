def solution():
    """The P.T.O. decided to provide shirts for the elementary students for track and field day. Each grade was given a different color. 101 Kindergartners wore orange shirts that cost $5.80 each. 113 first graders wore yellow shirts that cost $5 each. 107 second graders wore blue shirts that cost $5.60 each. 108 third graders wore green shirts that cost $5.25 each. How much did the P.T.O. spend on shirts for field day?"""
    # Define the number of students and the cost of each shirt for each grade
    num_kindergarten = 101
    cost_kindergarten = 5.8
    num_first_grade = 113
    cost_first_grade = 5
    num_second_grade = 107
    cost_second_grade = 5.6
    num_third_grade = 108
    cost_third_grade = 5.25

    # Calculate the total cost of shirts for each grade and add them together
    total_cost = (num_kindergarten * cost_kindergarten) + \
                 (num_first_grade * cost_first_grade) + \
                 (num_second_grade * cost_second_grade) + \
                 (num_third_grade * cost_third_grade)

    # Round the total cost to two decimal places
    result = round(total_cost, 2)
    return result

print(solution())