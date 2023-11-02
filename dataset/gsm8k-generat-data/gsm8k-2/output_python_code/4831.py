def solution():
    """In a 100-item exam, Lowella got 35% of the questions correctly. Pamela got 20% more correct answers than Lowella and Mandy got twice Pamela's score. What is Mandy’s score?"""
    total_items = 100
    lowella_score = 0.35 * total_items
    pamela_score = 1.2 * lowella_score
    mandy_score = 2 * pamela_score
    result = mandy_score
    return result

print(solution())