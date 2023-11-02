def solution():
    number_of_phrases_known = 17
    phrases_learned_per_week = 2
    phrases_known_when_bought = 3
    total_phrases_learned = number_of_phrases_known - phrases_known_when_bought
    number_of_weeks = total_phrases_learned / phrases_learned_per_week
    number_of_days = number_of_weeks * 7
    result = number_of_days
    return result

print(solution())