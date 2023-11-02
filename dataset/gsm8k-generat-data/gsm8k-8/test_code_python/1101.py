def solution():
    # Define Beckett's age
    beckett_age = 12

    # Calculate Olaf's age
    olaf_age = beckett_age + 3

    # Calculate Shannen's age
    shannen_age = olaf_age - 2

    # Calculate Jack's age
    jack_age = 5 + 2 * shannen_age

    # Calculate the sum of all four ages
    age_sum = beckett_age + olaf_age + shannen_age + jack_age
    result = age_sum
    return result

print(solution())