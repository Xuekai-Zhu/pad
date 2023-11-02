def solution():
    """Diane shows Sarah a game that deciphers at what age she will marry based on her name and current age. Sarah is 9 years old. The game consists of adding the number of letters in the player's name plus twice the player's age. According to the game, at what age will Sarah get married?"""
    # Define Sarah's current age and name
    current_age = 9
    name = "Sarah"

    # Calculate the age at which Sarah will supposedly get married
    marriage_age = len(name) + 2*current_age

    # return the result
    result = marriage_age
    return result

print(solution())