def solution():
    """Samantha’s last name has three fewer letters than Bobbie’s last name. If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie’s. Jamie’s full name is Jamie Grey. How many letters are in Samantha’s last name?"""
    letters_in_bobbie = 9
    letters_in_samantha = letters_in_bobbie - 3
    letters_in_jamie = 4
    letters_in_bobbie_reduced = letters_in_bobbie - 2
    result = letters_in_samantha
    return result

print(solution())