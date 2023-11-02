def solution():
    """Johnny is picking up the toys on the floor of his room. He'd dumped a lego boxed set with 500 pieces on the floor,
    and another one that had 3 times more pieces than the 500 piece one, and another one that had 1/4 the number of pieces.
    How many blocks does Johnny pick up if he picks up all the legos?"""
    first_box = 500
    second_box = 3 * first_box
    third_box = first_box / 4
    total_legos = first_box + second_box + third_box
    result = total_legos
    return result

def solution():
    """Samantha's last name has three fewer letters than Bobbie's last name. If Bobbie took two letters off her last name,
    she would have a last name twice the length of Jamie's. Jamie's full name is Jamie Grey. How many letters are in Samantha's last name?"""
    jamie_name_length = len("Grey")
    bobbie_name_length = jamie_name_length * 2 + 2
    samantha_name_length = bobbie_name_length - 3
    result = samantha_name_length
    return result

print(solution())