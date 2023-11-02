def solution():
    # Define the number of colors Tabitha will have in three years
    future_colors = 8

    # Calculate the number of colors she had when she started the tradition
    starting_colors = future_colors - 6

    # Calculate the age at which she started the tradition
    starting_age = 15 - 2

    # Calculate Tabitha's current age
    current_age = starting_age + starting_colors

    result = current_age
    return result

print(solution())