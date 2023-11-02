def solution():
    total_items = 100  # there are 100 items in the exam
    lowella_score = 0.35 * total_items  # Lowella got 35% of the answers correct
    pamela_score = 1.2 * lowella_score  # Pamela got 20% more correct answers than Lowella
    mandy_score = 2 * pamela_score  # Mandy got twice Pamela's score

    result = mandy_score
    return result

print(solution())