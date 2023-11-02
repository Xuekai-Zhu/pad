def solution():
    starting_color = "black"
    desired_color = "red"
    # Check if the desired color is lighter than the starting color
    if desired_color < starting_color:
        result = "no"
    else:
        result = "yes, you need to bleach the hair"
    return result

print(solution())