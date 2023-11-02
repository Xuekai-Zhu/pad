def solution():
    total_toys = 160  # Total number of toys
    difference = 30  # Anais has 30 more toys than Kamari

    # Formulating equations
    # A + K = total_toys
    # A - K = difference
    # Solving the equations simultaneously
    kamari_toys = (total_toys - difference) / 2
    result = kamari_toys
    return result

print(solution())