def solution():
    # Define the given information
    num_siblings = 14
    kay_age = 32
    youngest_sib_age = 0.5 * kay_age - 5
    oldest_sib_age = 4 * youngest_sib_age

    # Find the total age of all the siblings
    total_sib_age = (num_siblings + 1) * kay_age

    # Subtract Kay's age and the youngest sibling's age to find the total age of the other siblings
    other_sib_age = total_sib_age - kay_age - youngest_sib_age

    # Subtract the total age of the other siblings from the total age of all the siblings to find the age of the oldest sibling
    oldest_sib_age = total_sib_age - other_sib_age - kay_age - youngest_sib_age
    result = oldest_sib_age
    return result

print(solution())