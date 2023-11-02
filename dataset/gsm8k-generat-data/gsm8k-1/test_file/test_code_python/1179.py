def solution():
    """Samantha's last name has three fewer letters than Bobbie's last name. If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie's. Jamie's full name is Jamie Grey. How many letters are in Samantha's last name?"""
    jamies_last_name = "Grey"
    bobbies_last_name = len(jamies_last_name) * 2 + 2  # Bobbie's last name is twice Jamie's last name plus two letters
    samanthas_last_name = bobbies_last_name - 3  # Samantha's last name has three fewer letters than Bobbie's
    result = samanthas_last_name
    return result


def solution():
    """Two apples fell out of the tree, and one of them landed on Newton's head. Newton picked up the two apples, put one in his pocket and threw the other apple into the tree, causing 5 more apples to fall out of the tree. Newton picked up these apples, put all but one in his pocket and threw the remaining one at the tree. This caused another 6 apples to fall out of the tree. Newton picked up all of the remaining apples and went home to make a pie. How many apples did he bring home?"""
    initial_apples = 2
    apples_pocketed = 1
    thrown_apples = 2
    thrown_apples_caused = 5 + 1  # 5 more apples fell from the tree plus the one Newton threw
    remaining_apples = thrown_apples_caused - apples_pocketed
    thrown_apples_2 = 1
    thrown_apples_caused_2 = 6
    remaining_apples_2 = thrown_apples_caused_2 - (remaining_apples + apples_pocketed)
    total_apples = remaining_apples_2 + apples_pocketed
    result = total_apples
    return result

print(solution())