def solution():
    beckett_age = 12

    # Determine Olaf's age
    olaf_age = beckett_age + 3

    # Determine Shannen's age
    shannen_age = olaf_age - 2

    # Determine Jack's age
    jack_age = 2 * shannen_age + 5

    # Calculate the sum of all ages
    total_age = beckett_age + olaf_age + shannen_age + jack_age
    result = total_age
    return result

print(solution())