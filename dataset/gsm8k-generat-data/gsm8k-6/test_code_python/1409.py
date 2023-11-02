def solution():
    # Calculate the total number of books Quinn read
    total_books = 2 * 10  # Quinn can read 2 books a week for 10 weeks
    # Calculate the number of coupons Quinn can receive
    num_coupons = total_books // 5  # Quinn receives a coupon for every 5 books read
    result = num_coupons
    return result

print(solution())