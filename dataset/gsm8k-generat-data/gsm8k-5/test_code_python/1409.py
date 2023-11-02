def solution():
    books_per_coupon = 5  # Quinn needs to read 5 books to get 1 coupon for a free donut
    books_per_week = 2  # Quinn can read 2 books per week
    total_weeks = 10  # Quinn will be reading for 10 weeks

    # Calculate the total number of books Quinn will read
    total_books = books_per_week * total_weeks

    # Calculate the total number of coupons Quinn will receive
    total_coupons = total_books // books_per_coupon

    result = total_coupons
    return result

print(solution())