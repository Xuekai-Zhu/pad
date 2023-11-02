def solution():
    """Bob grew corn in his garden and is ready to harvest it. He has 5 rows of corn, and each row has 80 corn stalks. About every 8 corn stalks will produce a bushel of corn. How many bushels of corn will Bob harvest?"""
    # Define the number of rows and corn stalks per row
    rows = 5
    corn_per_row = 80

    # Calculate the total number of corn stalks
    total_corn_stalks = rows * corn_per_row

    # Calculate the number of bushels of corn
    bushels_of_corn = total_corn_stalks // 8

    result = bushels_of_corn
    return result

print(solution())