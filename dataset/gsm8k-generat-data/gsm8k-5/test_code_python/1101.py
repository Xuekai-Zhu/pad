def solution():
    # Olaf's age
    olaf = 12 + 3  # Beckett is 3 years younger than Olaf

    # Shannen's age
    shannen = olaf - 2  # Shannen is 2 years younger than Olaf

    # Jack's age
    jack = 5 + 2 * shannen  # Jack is 5 more than twice as old as Shannen

    # Total sum of ages
    total_sum = 12 + olaf + shannen + jack
    result = total_sum
    return result

print(solution())