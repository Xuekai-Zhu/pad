def solution():
    """The P.T.O. decided to provide shirts for the elementary students for track and field day. Each grade was given a different color. 101 Kindergartners wore orange shirts that cost $5.80 each. 113 first graders wore yellow shirts that cost $5 each. 107 second graders wore blue shirts that cost $5.60 each. 108 third graders wore green shirts that cost $5.25 each. How much did the P.T.O. spend on shirts for field day?"""
    # Define the cost and number of shirts for each grade
    KINDERGARTEN_COST = 5.80
    FIRST_GRADE_COST = 5.00
    SECOND_GRADE_COST = 5.60
    THIRD_GRADE_COST = 5.25

    KINDERGARTEN_SHIRTS = 101
    FIRST_GRADE_SHIRTS = 113
    SECOND_GRADE_SHIRTS = 107
    THIRD_GRADE_SHIRTS = 108

    # Calculate the total cost
    total_cost = (KINDERGARTEN_COST * KINDERGARTEN_SHIRTS) + (FIRST_GRADE_COST * FIRST_GRADE_SHIRTS) + (SECOND_GRADE_COST * SECOND_GRADE_SHIRTS) + (THIRD_GRADE_COST * THIRD_GRADE_SHIRTS)

    # Display the total cost
    result = total_cost
    return result

print(solution())