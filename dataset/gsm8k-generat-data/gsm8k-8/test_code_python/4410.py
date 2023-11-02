def solution():
    # Define the number of rows and stalks per row
    num_rows = 5
    stalks_per_row = 80

    # Calculate the total number of corn stalks
    total_stalks = num_rows * stalks_per_row

    # Calculate the number of bushels based on the ratio of corn stalks to bushels
    ratio = 8
    num_bushels = total_stalks // ratio

    result = num_bushels
    return result

print(solution())