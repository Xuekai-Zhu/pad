def solution():
    total_hoodies = 8  # Fiona and Casey own a total of 8 hoodies
    diff = 2  # Casey owns 2 more hoodies than Fiona

    # Calculate the number of hoodies Fiona owns
    fiona_hoodies = (total_hoodies - diff) / 2

    result = fiona_hoodies
    return result

print(solution())