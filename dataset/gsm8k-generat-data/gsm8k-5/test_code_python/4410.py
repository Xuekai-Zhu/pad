def solution():
    rows_of_corn = 5  # Bob has 5 rows of corn
    corn_per_row = 80  # Each row has 80 corn stalks
    corn_for_bushel = 8  # About 8 corn stalks will produce one bushel

    # Calculate the total number of corn stalks and the number of bushels
    total_corn_stalks = rows_of_corn * corn_per_row
    bushels_of_corn = total_corn_stalks // corn_for_bushel

    result = bushels_of_corn
    return result

print(solution())