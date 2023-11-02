def solution():
    # Calculate the percentage of people who said they are not voting for Biff
    not_biff_percentage = 100 - 45 - 8

    # Calculate the number of people who said they are not voting for Biff
    not_biff_count = 200 * not_biff_percentage / 100

    # Calculate the number of people who said they are voting for Marty
    marty_count = not_biff_count

    result = marty_count
    return result

print(solution())