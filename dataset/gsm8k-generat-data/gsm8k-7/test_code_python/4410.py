def solution():
    num_rows = 5
    corn_per_row = 80
    corn_for_bushel = 8

    # Calculate the total number of corn stalks
    total_corn_stalks = num_rows * corn_per_row

    # Calculate the total number of bushels of corn
    total_bushels = total_corn_stalks / corn_for_bushel
    result = total_bushels
    return result

print(solution())