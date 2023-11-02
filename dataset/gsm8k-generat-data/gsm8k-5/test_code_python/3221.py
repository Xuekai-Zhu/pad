def solution():
    kay_age = 32  # Kay is 32 years old
    youngest_sibling_age = (kay_age / 2) - 5  # Youngest sibling is 5 less than half of Kay's age
    oldest_sibling_age = 4 * youngest_sibling_age  # Oldest sibling is four times as old as the youngest sibling

    # Calculate the age of the oldest sibling
    for i in range(1, 15):
        if i != 1 and i != 14:
            oldest_sibling_age += youngest_sibling_age
        else:
            continue
    result = oldest_sibling_age
    return result

print(solution())