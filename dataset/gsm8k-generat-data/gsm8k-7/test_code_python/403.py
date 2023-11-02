def solution():
    kimiko_age = 28
    omi_age = 2 * kimiko_age
    arlette_age = 0.75 * kimiko_age

    # Calculate the total age of the three individuals
    total_age = kimiko_age + omi_age + arlette_age

    # Calculate the average age of the three individuals
    average_age = total_age / 3
    result = average_age
    return result

print(solution())