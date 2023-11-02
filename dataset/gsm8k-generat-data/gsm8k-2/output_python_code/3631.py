def solution():
    """James buys 2 notebooks with 50 pages each. He pays $5. How many cents did each page cost?"""
    total_pages = 2 * 50
    total_paid = 500  # in cents
    price_per_page = total_paid / total_pages
    result = price_per_page
    return result

print(solution())