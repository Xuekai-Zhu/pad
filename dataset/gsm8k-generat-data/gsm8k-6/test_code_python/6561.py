def solution():
    # Calculate the length of rope Bob has left after making the art piece and giving half to his friend
    remaining_rope = (4/5) * 50 / 2  # Bob uses 1/5 of the rope and gives half of the remaining rope to his friend
    # Calculate the number of 2-foot sections he can cut from the remaining rope
    sections = remaining_rope / 2
    result = sections
    return result

print(solution())