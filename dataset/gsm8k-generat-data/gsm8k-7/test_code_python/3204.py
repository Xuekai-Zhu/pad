def solution():
    num_eggs = 2 * 12  # Mark has 2 dozen eggs, which is 24 eggs total

    num_people = 3 + 1  # Mark has 3 siblings plus himself

    # Calculate the number of eggs each person gets by dividing the total number of eggs by the number of people
    num_eggs_per_person = num_eggs / num_people
    result = num_eggs_per_person
    return result

print(solution())