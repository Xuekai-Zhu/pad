def solution():
    # Define Maude's age
    maude_age = 8

    # Calculate Emile's age when Anne is two times as old
    emile_age = 6 * maude_age / 5

    # Calculate Anne's age at that time
    anne_age = 2 * emile_age

    # Calculate Anne's current age
    current_anne_age = anne_age - emile_age

    result = current_anne_age
    return result

print(solution())