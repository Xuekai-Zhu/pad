def solution():
    """Bob grew corn in his garden and is ready to harvest it. He has 5 rows of corn, and each row has 80 corn stalks. About every 8 corn stalks will produce a bushel of corn. How many bushels of corn will Bob harvest?"""
    # Define the number of rows and corn stalks per row
    rows = 5
    stalks_per_row = 80

    # Calculate the total number of corn stalks
    total_stalks = rows * stalks_per_row

    # Calculate the number of bushels of corn
    bushels = total_stalks // 8

    # Display the number of bushels
    result = bushels
    return result

print(solution())