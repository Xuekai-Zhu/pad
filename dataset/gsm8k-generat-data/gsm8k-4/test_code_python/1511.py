def solution():
    """Janice opened an art book that she had found in the library and found 5 drawings on the first page. After opening the first ten pages, she realized that the number of drawings on each page increased by five after every page. How many drawings were in the first five pages?"""
    # Define the number of drawings on the first page and the increase per page
    initial_drawings = 5
    increase_per_page = 5

    # Initialize the page counter and the total number of drawings
    page = 1
    total_drawings = initial_drawings

    # Add the number of drawings on each page to the total, up to the fifth page
    while page < 5:
        # Increment the page counter
        page += 1
        
        # Calculate the number of drawings on the current page
        drawings_on_page = initial_drawings + (page - 1) * increase_per_page
        
        # Add the number of drawings to the total
        total_drawings += drawings_on_page

    # Return the result
    result = total_drawings
    return result

print(solution())