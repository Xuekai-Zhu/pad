def solution():
    """James runs a TV show and there are 5 main characters and 4 minor characters. He pays the minor characters $15,000 each episode. He paid the major characters three times as much. How much does he pay per episode?"""
    num_minor_characters = 4
    num_major_characters = 5
    minor_character_pay = 15000
    major_character_pay = 3 * minor_character_pay
    total_pay = (num_minor_characters * minor_character_pay) + (num_major_characters * major_character_pay)
    result = total_pay
    return result

print(solution())