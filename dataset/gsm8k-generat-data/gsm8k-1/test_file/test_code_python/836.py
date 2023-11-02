def solution():
    """Patrick has three glue sticks that are partially used. One has 1/6 left, the second has 2/3 left and the third one has 1/2 left. If a glue stick is 12 millimeters long originally, what is the total length of the glue sticks that are not used?"""
    full_length = 12
    used_lengths = [(1/6)*full_length, (2/3)*full_length, (1/2)*full_length]
    unused_lengths = [full_length - length for length in used_lengths]
    total_unused_length = sum(unused_lengths)
    result = total_unused_length
    return result

print(solution())