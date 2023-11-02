def solution():
    # Calculate the total number of orange pieces
    total_pieces = 5 * 8  # James breaks each orange into 8 pieces and has 5 oranges

    # Calculate the total number of calories
    total_calories = total_pieces * 80  # Each orange piece has 80 calories

    # Calculate the calories per person
    calories_per_person = total_calories / 4  # The pieces are split between 4 people

    result = calories_per_person
    return result

print(solution())