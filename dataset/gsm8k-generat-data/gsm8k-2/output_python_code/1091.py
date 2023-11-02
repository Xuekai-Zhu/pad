def solution():
    """Estevan has 24 blankets. One-third of the blankets have polka-dots. For his birthday, his mother gives him 2 more polka-dot print blankets. How many polka-dot blankets does Estevan have in total?"""
    total_blankets = 24
    polka_dot_blankets = total_blankets // 3
    new_polka_dot_blankets = 2
    total_polka_dot_blankets = polka_dot_blankets + new_polka_dot_blankets
    result = total_polka_dot_blankets
    return result

print(solution())