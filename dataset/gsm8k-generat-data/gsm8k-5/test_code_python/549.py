def solution():
    # Calculate the total number of legs on the chairs
    total_chair_legs = 80 * 5

    # Calculate the total number of legs on the tables
    total_table_legs = 20 * 3

    # Calculate the total number of chairs to be disposed of
    disposed_chairs = 0.4 * 80

    # Calculate the new total number of chairs
    remaining_chairs = 80 - disposed_chairs

    # Calculate the new total number of chair legs
    remaining_chair_legs = remaining_chairs * 5

    # Calculate the total number of remaining furniture legs
    total_legs_remaining = remaining_chair_legs + total_table_legs

    result = total_legs_remaining
    return result

print(solution())