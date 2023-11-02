def solution():
    num_tubs = 6  # Marcy brings 6 tubs of lip gloss
    num_tubes_per_tub = 2  # Each tub holds 2 tubes of lip gloss
    num_people_per_tube = 3  # Each tube of lip gloss is enough for 3 people's makeup

    # Calculate the total number of people Marcy is painting with makeup
    total_people = num_tubs * num_tubes_per_tub * num_people_per_tube
    result = total_people
    return result

print(solution())