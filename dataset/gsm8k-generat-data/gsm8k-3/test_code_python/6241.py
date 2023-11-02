def solution():
    """James takes 5 oranges and breaks each orange into 8 pieces.  He splits the pieces between 4 people.  If an orange has 80 calories how many calories does each person get?"""
    # Define the number of oranges and pieces per orange
    NUM_ORANGES = 5
    PIECES_PER_ORANGE = 8

    # Calculate the total number of pieces
    total_pieces = NUM_ORANGES * PIECES_PER_ORANGE

    # Calculate the total number of calories
    total_calories = total_pieces * 80

    # Calculate the number of calories per person
    calories_per_person = total_calories / 4

    # Display the number of calories per person
    result = calories_per_person
    return result

print(solution())