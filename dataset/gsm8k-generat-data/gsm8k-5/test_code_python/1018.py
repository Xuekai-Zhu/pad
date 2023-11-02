def solution():
    couples = 3  # There are 3 couples in the book club
    single_people = 5  # There are 5 single people in the book club
    total_members = (2 * couples) + single_people + 2  # Ron and his wife are also members

    # Calculate the number of times Ron gets to pick a new book per year
    books_per_year = 52  # There are 52 weeks in a year
    times_picking_per_year = 1 / total_members * books_per_year
    result = times_picking_per_year
    return result

print(solution())