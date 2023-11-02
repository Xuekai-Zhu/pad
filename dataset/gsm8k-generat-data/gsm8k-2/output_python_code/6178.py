def solution():
    """Diane shows Sarah a game that deciphers at what age she will marry based on her name and current age. Sarah is 9 years old. The game consists of adding the number of letters in the player's name plus twice the player's age. According to the game, at what age will Sarah get married?"""
    name_length = len("Sarah")
    age = 9
    marriage_age = (name_length + (2 * age)) % 50
    result = marriage_age
    return result

print(solution())