def solution():
    # Calculate the total number of eyeshadow colors Amy had
    total_colors = 2*4 + 3*6  # two eyeshadow palettes with 4 colors each and three makeup sets with 6 colors each

    # Calculate the number of eyeshadow colors Amy uses up from one makeup set
    used_colors = 1/2 * total_colors  # Amy uses up half of the colors from one makeup set

    # Calculate the number of eyeshadow colors Amy has left
    remaining_colors = total_colors - used_colors
    result = remaining_colors
    return result

print(solution())