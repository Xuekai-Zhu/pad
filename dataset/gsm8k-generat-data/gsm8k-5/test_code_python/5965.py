def solution():
    legs_per_horse = 4  # Horses have 4 legs
    legs_per_dog = 4  # Dogs have 4 legs
    legs_per_cat = 4  # Cats have 4 legs
    legs_per_turtle = 4  # Turtles have 4 legs
    legs_per_goat = 4  # Goats have 4 legs

    total_legs = (2 * legs_per_horse) + (5 * legs_per_dog) + (7 * legs_per_cat) + (3 * legs_per_turtle) + legs_per_goat
    result = total_legs
    return result

print(solution())