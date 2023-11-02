def solution():
    total_people = 30 + 20  # Total number of people at the party
    fraction_left = 2/5  # Fraction of people who left the party
    people_left = fraction_left * total_people  # Number of people who left the party
    remaining_men = 20 - 9  # Number of men who stayed at the party
    remaining_women = 30 - people_left - remaining_men  # Number of women who stayed at the party

    # Calculate the difference between the number of remaining women and men
    difference = remaining_women - remaining_men
    result = difference
    return result

print(solution())