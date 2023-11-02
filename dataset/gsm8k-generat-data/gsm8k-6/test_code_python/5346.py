def solution():
    # Calculate the total number of books Henry has after decluttering and taking some back
    starting_books = 99   # starting number of books
    boxes_donated = 3 * 15  # number of books donated in boxes
    other_donations = 21 + 4 + 18  # number of books donated from other places
    taken_back = 12  # number of books Henry took back
    total_books = starting_books - boxes_donated - other_donations + taken_back  # total books now
    result = total_books
    return result

print(solution())