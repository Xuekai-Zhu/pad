def solution():
    
    # Define the number of basketball cards in each deck and box
    basketball_cards = 25
    box_cards = 40

    # Define the number of cards Miss Maria has
    total_cards = (6 * basketball_cards) + (5 * box_cards)

    # Define the number of cards Miss Maria keeps
    cards_kept = 50

    # Define the number of cards Miss Maria gives to her students
    cards_given = 10

    # Calculate the number of students Miss Maria has
    students = total_cards - cards_kept

    # Display the number of students
    result = students
    return result

print(solution())