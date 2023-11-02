def solution():
    # Define the total number of sheep and the fraction that Mary gave to her sister
    total_sheep = 400
    sister_fraction = 0.25

    # Calculate the number of sheep that Mary gave to her sister and the number that remain
    sheep_to_sister = total_sheep * sister_fraction
    sheep_remaining = total_sheep - sheep_to_sister

    # Calculate the fraction of remaining sheep that Mary gave to her brother
    brother_fraction = 0.5
    sheep_to_brother = sheep_remaining * brother_fraction

    # Calculate the number of sheep that remain with Mary
    sheep_remaining = sheep_remaining - sheep_to_brother

    result = sheep_remaining
    return result

print(solution())