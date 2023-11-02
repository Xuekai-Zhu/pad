def solution():
    cannoneers = 63  # There were 63 cannoneers in the battle
    women = cannoneers * 2  # There were 2 women for every cannoneer
    men = women * 2  # The total number of men was twice the number of women

    # Calculate the total number of people in the battle
    total_people = cannoneers + women + men
    result = total_people
    return result

print(solution())