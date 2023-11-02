def solution():
    # Calculate how many books Evan owns now
    evan_now = 200 - 2 - 40  # Evan had 200 books 2 years ago, and currently owns 40 fewer books than he had 2 years ago

    # Calculate how many books Evan will have in five years
    evan_in_5_years = 5 * (evan_now + 60)  # Evan will have 60 more than five times as many books as he owns now in five years

    # Calculate the total number of books Evan will have in five years
    total_books_in_5_years = evan_in_5_years + evan_now
    result = total_books_in_5_years
    return result

print(solution())