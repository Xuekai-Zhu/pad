def solution():
    """Ryanne is 7 years older than Hezekiah. Together Ryanne's and Hezekiah's ages equal 15 years. How many years old is Hezekiah?"""
    total_age = 15
    age_difference = 7
    ryanne_age = (total_age + age_difference) / 2
    hezekiah_age = total_age - ryanne_age
    result = hezekiah_age
    return result

print(solution())