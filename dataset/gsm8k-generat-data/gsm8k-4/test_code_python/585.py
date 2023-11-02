def solution():
    """Maddy's 4th grade class needs to make 1000 Valentine's Day cards to get a pizza party. There are 30 kids in the class. If everyone makes 8, how many more cards will they need to make to get a pizza party?"""
    # Define the number of students and the number of cards per student
    num_students = 30
    cards_per_student = 8

    # Calculate the total number of cards made by the students
    total_cards_made = num_students * cards_per_student

    # Calculate the number of cards needed to reach the goal
    cards_needed = 1000 - total_cards_made

    # return the result
    result = cards_needed
    return result

print(solution())