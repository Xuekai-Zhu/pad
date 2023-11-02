def solution():
    """Jairus read 20 pages of the newspaper. Arniel read 2 more than twice the number of pages Jairus read. How many pages have they read altogether?"""
    # Define the number of pages Jairus read
    jairus_pages = 20

    # Calculate the number of pages Arniel read
    arniel_pages = 2 + 2 * jairus_pages

    # Calculate the total number of pages they read together
    total_pages = jairus_pages + arniel_pages

    # return the result
    result = total_pages
    return result

print(solution())