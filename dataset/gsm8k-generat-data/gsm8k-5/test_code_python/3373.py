def solution():
    # Total number of people in the Easter egg hunt
    total_people = 2 + 10 + 2 + 7  # Shonda's 2 kids, 10 friends, Shonda and 7 other adults

    # Total number of Easter eggs available
    total_eggs = 15 * 12  # 15 baskets each holding 12 eggs

    # Number of eggs each person gets when equally distributed
    eggs_per_person = total_eggs / total_people

    result = eggs_per_person
    return result

print(solution())