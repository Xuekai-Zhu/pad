def solution():
    total_books = 99

    # Calculate the number of books donated in boxes
    box_donation = 3 * 15

    # Calculate the number of books donated from other areas
    other_donation = 21 + 4 + 18

    # Calculate the total number of books donated
    total_donation = box_donation + other_donation

    # Calculate the number of books taken from the free box
    free_box = 12

    # Calculate the remaining number of books Henry has
    remaining_books = total_books - total_donation + free_box
    result = remaining_books
    return result

print(solution())