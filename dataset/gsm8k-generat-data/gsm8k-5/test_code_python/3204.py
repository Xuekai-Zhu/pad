def solution():
    eggs_per_dozen = 12  # There are 12 eggs in a dozen
    total_eggs = 2 * eggs_per_dozen  # Mark has 2 dozen eggs
    siblings = 3  # Mark has 3 siblings

    # Calculate how many eggs each person gets to eat
    eggs_per_person = total_eggs / (siblings + 1)  # Mark is also a person in this context

    result = eggs_per_person
    return result

print(solution())