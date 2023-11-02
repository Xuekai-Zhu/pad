def solution():
    num_books_per_week = 2
    num_weeks = 10

    # Calculate the total number of books that Quinn will read
    total_books = num_books_per_week * num_weeks

    # Calculate the total number of free donut coupons that Quinn will earn
    num_donuts = total_books // 5
    result = num_donuts
    return result

print(solution())