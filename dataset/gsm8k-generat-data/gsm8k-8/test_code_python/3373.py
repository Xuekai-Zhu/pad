def solution():
    # Calculate the total number of people searching for eggs
    total_people = 2 + 10 + 7

    # Calculate the total number of eggs available
    total_eggs = 15 * 12

    # Calculate the number of eggs each person gets
    eggs_per_person = total_eggs / total_people
    result = eggs_per_person
    return result

print(solution())