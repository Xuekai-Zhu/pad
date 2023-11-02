def solution():
    """Estevan has 24 blankets. One-third of the blankets have polka-dots. For his birthday, his mother gives him 2 more polka-dot print blankets. How many polka-dot blankets does Estevan have in total?"""
    # Define the total number of blankets and the fraction with polka dots
    total_blankets = 24
    polka_dot_fraction = 1/3

    # Calculate the number of blankets with polka dots
    polka_dot_blankets = polka_dot_fraction * total_blankets

    # Add the 2 new polka dot blankets
    total_polka_dot_blankets = polka_dot_blankets + 2

    # Display the total number of polka dot blankets
    result = total_polka_dot_blankets
    return result

print(solution())