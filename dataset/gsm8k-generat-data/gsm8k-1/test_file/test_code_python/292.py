def solution():
    """Each person in a certain household consumes 0.2 kg of rice every meal. Supposing 5 members of the household eat rice every lunch and dinner, how many weeks will a 42 kg bag of rice last?"""
    rice_per_meal_per_person = 0.2
    meals_per_day_per_person = 2
    persons_per_household = 5
    total_rice_per_day = rice_per_meal_per_person * meals_per_day_per_person * persons_per_household
    total_weeks = 42 / (total_rice_per_day * 7)
    result = total_weeks
    return result

print(solution())