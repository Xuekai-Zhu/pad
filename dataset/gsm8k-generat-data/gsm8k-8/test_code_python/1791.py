def solution():
    # Calculate the number of delegates with pre-printed name badges
    printed_name_badges = 16

    # Calculate the number of delegates without printed name badges
    remaining_delegates = 36 - printed_name_badges

    # Calculate the number of delegates who made their own name badges
    handmade_name_badges = remaining_delegates // 2

    # Calculate the number of delegates without name badges
    no_badges = remaining_delegates - handmade_name_badges

    result = no_badges
    return result

print(solution())