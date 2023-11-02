def solution():
    """Joseph gave 23 cards to each of his 15 students and had 12 cards left. How many cards did Joseph have at first?"""
    # Define the variables
    cards_per_student = 23
    number_of_students = 15
    left_over_cards = 12

    # Calculate the total number of cards given out
    total_cards_given_out = cards_per_student * number_of_students

    # Calculate the total number of cards Joseph had at first
    total_cards_at_first = total_cards_given_out + left_over_cards

    # Display the total number of cards Joseph had at first
    result = total_cards_at_first
    return result

print(solution())