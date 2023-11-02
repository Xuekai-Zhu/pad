def solution():
    oranges = 5
    pieces_per_orange = 8
    total_pieces = oranges * pieces_per_orange
    people = 4

    # Calculate the total number of calories from all the pieces of oranges
    total_calories = total_pieces * 80

    # Calculate the number of calories each person gets
    calories_per_person = total_calories / people
    result = calories_per_person
    return result

print(solution())