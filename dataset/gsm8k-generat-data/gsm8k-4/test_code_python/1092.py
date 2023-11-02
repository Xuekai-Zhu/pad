def solution():
    """Estevan has 24 blankets. One-third of the blankets have polka-dots. For his birthday, his mother gives him 2 more polka-dot print blankets. How many polka-dot blankets does Estevan have in total?"""
    # Define the total number of blankets
    total_blankets = 24

    # Calculate the number of polka-dot blankets
    polka_dot_blankets = total_blankets * (1/3)

    # Add the 2 new polka-dot blankets from Estevan's mother
    polka_dot_blankets += 2

    result = polka_dot_blankets
    return result

print(solution())