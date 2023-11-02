def solution():
    # Define the necessary information
    has_doctorate = False
    first_book_published = 1937
    doctorate_earned = 1956
    # Check if Dr. Seuss lied about having a doctorate
    if has_doctorate or doctorate_earned <= first_book_published:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())