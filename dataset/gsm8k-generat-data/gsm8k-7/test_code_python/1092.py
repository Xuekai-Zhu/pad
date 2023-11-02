def solution():
    total_blankets = 24
    polka_dot_fraction = 1/3
    extra_polka_dot_blankets = 2

    # Calculate the number of polka-dot blankets Estevan had originally
    num_polka_dot_blankets = total_blankets * polka_dot_fraction

    # Add the two extra polka-dot blankets
    total_polka_dot_blankets = num_polka_dot_blankets + extra_polka_dot_blankets
    result = total_polka_dot_blankets
    return result

print(solution())