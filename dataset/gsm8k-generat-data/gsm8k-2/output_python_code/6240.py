def solution():
    """James takes 5 oranges and breaks each orange into 8 pieces. He splits the pieces between 4 people. If an orange has 80 calories how many calories does each person get?"""
    oranges = 5
    pieces_per_orange = 8
    total_pieces = oranges * pieces_per_orange
    people = 4
    pieces_per_person = total_pieces / people
    calories_per_piece = 80
    calories_per_person = calories_per_piece * pieces_per_person
    result = calories_per_person
    return result

print(solution())