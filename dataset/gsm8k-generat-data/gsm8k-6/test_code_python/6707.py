def solution():
    # Calculate the number of sheep given to Mary's sister
    sister_sheep = 400 * 0.25

    # Calculate the number of sheep remaining with Mary
    remaining_sheep = 400 - sister_sheep

    # Calculate the number of sheep given to Mary's brother
    brother_sheep = remaining_sheep * 0.5

    # Calculate the number of sheep remaining with Mary after giving to her sister and brother
    remaining_sheep = remaining_sheep - brother_sheep

    result = remaining_sheep
    return result

print(solution())