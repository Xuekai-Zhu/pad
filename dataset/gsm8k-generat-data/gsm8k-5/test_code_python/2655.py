def solution():
    total_decorations = 15  # Trey used 15 sticky strips
    fraction_nails = 2/3  # Trey used nails for two-thirds of all decorations
    fraction_thumbtacks = 2/5  # Trey used thumbtacks for two-fifths of the remaining decorations
    fraction_sticky_strips = 1 - fraction_nails - fraction_thumbtacks  # Trey used sticky strips for the remaining decorations

    # Calculate the number of decorations that required nails
    num_nail_decorations = int(fraction_nails * total_decorations)

    # Calculate the number of decorations that required thumbtacks
    num_thumbtack_decorations = int(fraction_thumbtacks * (total_decorations - num_nail_decorations))

    # Calculate the number of decorations that required sticky strips
    num_sticky_strip_decorations = total_decorations - num_nail_decorations - num_thumbtack_decorations

    # Calculate the number of nails Trey used
    num_nails = num_nail_decorations

    result = num_nails
    return result

print(solution())