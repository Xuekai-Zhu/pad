def solution():
    """Joseph gave 23 cards to each of his 15 students and had 12 cards left. How many cards did Joseph have at first?"""
    # Define the number of students and the number of cards each student received
    num_students = 15
    num_cards_per_student = 23

    # Calculate the total number of cards distributed to the students
    total_cards_distributed = num_students * num_cards_per_student

    # Calculate the number of cards Joseph had left
    num_cards_left = 12

    # Calculate the total number of cards Joseph had at first
    total_cards_at_first = total_cards_distributed + num_cards_left

    result = total_cards_at_first
    return result

print(solution())