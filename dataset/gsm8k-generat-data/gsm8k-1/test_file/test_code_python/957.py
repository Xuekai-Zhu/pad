def solution():
    """Samantha's last name has three fewer letters than Bobbie's last name. If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie's. Jamie's full name is Jamie Grey. How many letters are in Samantha's last name?"""
    jamie_name_length = len("Grey")
    bobbie_name_length = (jamie_name_length * 2) + 2
    samantha_name_length = bobbie_name_length - 3
    result = samantha_name_length
    return result


def solution():
    """Amora, Lainey, and Collins wanted to share corn chips equally but then realized only two people would get an equal amount of corn chips, while the other person would receive 15 more corn chips than the number the others got. If Amora and Lainey got 70 corn chips each, how many corn chips were there altogether?"""
    equal_chips = 70
    unequal_chips = equal_chips + 15
    total_chips = (equal_chips * 2) + unequal_chips
    result = total_chips
    return result

print(solution())