def solution():
    """James takes 5 oranges and breaks each orange into 8 pieces. He splits the pieces between 4 people. If an orange has 80 calories how many calories does each person get?"""
    # Define the number of oranges and pieces per orange
    oranges = 5
    pieces_per_orange = 8

    # Calculate the total number of pieces
    total_pieces = oranges * pieces_per_orange

    # Calculate the number of pieces per person
    pieces_per_person = total_pieces / 4

    # Calculate the number of calories per person
    calories_per_person = pieces_per_person * 80

    result = calories_per_person
    return result

print(solution())