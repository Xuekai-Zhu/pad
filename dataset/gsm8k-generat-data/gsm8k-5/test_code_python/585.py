def solution():
    cards_needed = 1000  # The class needs to make 1000 cards to get a pizza party
    students = 30  # There are 30 kids in the class
    cards_per_student = 8  # Each student needs to make 8 cards

    # Calculate the total number of cards made by the class
    cards_made = students * cards_per_student

    # Calculate the remaining number of cards needed to reach the goal
    remaining_cards = cards_needed - cards_made
    result = remaining_cards
    return result

print(solution())