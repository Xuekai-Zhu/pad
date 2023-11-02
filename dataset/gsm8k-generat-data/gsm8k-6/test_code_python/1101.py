def solution():
    # Find Olaf's age
    olaf_age = Beckett + 3  # Beckett is 3 years younger than Olaf
    shannen_age = olaf_age - 2  # Shannen is 2 years younger than Olaf
    jack_age = 5 + 2 * shannen_age  # Jack is 5 more than twice Shannen's age
    sum_of_ages = Beckett + olaf_age + shannen_age + jack_age
    result = sum_of_ages
    return result

print(solution())