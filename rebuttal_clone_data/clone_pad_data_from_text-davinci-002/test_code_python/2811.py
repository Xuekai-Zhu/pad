def solution():
    babies_given = 8 * 3 / 6
    babies_sold = 8 * 3 * 3
    babies_left = 8 * 3 - babies_given - babies_sold
    result = babies_left
    return result

print(solution())