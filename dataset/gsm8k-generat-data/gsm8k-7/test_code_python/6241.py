def solution():
    num_oranges = 5
    pieces_per_orange = 8
    num_people = 4
    calories_per_piece = 80

    # Calculate the total number of pieces of orange that James has
    total_pieces = num_oranges * pieces_per_orange

    # Calculate the total number of calories in all the pieces
    total_calories = total_pieces * calories_per_piece

    # Calculate the number of calories each person gets
    calories_per_person = total_calories / num_people
    result = calories_per_person
    return result

print(solution())