def solution():
    """Ron is part of a book club that allows each member to take a turn picking a new book every week. The club is made up of three couples and five single people along with Ron and his wife. How many times a year does Ron get to pick a new book?"""
    couples = 3
    singles = 5
    members = couples * 2 + singles + 2 # adding Ron and his wife
    weeks_per_year = 52
    books_per_year = weeks_per_year / members
    ron_books_per_year = books_per_year * 2 # Ron picks twice as often as a couple
    result = ron_books_per_year
    return result

print(solution())