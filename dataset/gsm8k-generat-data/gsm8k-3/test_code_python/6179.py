def solution():
    """Diane shows Sarah a game that deciphers at what age she will marry based on her name and current age.
    Sarah is 9 years old. The game consists of adding the number of letters in the player's name plus twice the player's age.
    According to the game, at what age will Sarah get married?"""
    # Define Sarah's current age and name
    age = 9
    name = "Sarah"

    # Calculate the number of letters in Sarah's name
    name_length = len(name)

    # Calculate Sarah's "marriage age" based on the game
    marriage_age = name_length + (2 * age)

    # Display Sarah's "marriage age"
    result = marriage_age
    return result

print(solution())