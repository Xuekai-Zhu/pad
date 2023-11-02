def solution():
    """Janice opened an art book that she had found in the library and found 5 drawings on the first page. After opening the first ten pages, she realized that the number of drawings on each page increased by five after every page. How many drawings were in the first five pages?"""
    # Define the number of drawings on the first page
    DRAWINGS_1 = 5

    # Define the number of drawings added to each page after the first page
    DRAWINGS_INCREMENT = 5

    # Define the total number of pages opened
    PAGES = 10

    # Calculate the total number of drawings on the first 10 pages
    total_drawings = 0
    for i in range(PAGES):
        total_drawings += DRAWINGS_1 + i * DRAWINGS_INCREMENT

    # Calculate the number of drawings on the first 5 pages
    first_5_pages = total_drawings - (DRAWINGS_1 + (PAGES-1)*DRAWINGS_INCREMENT)
    
    # Display the number of drawings on the first 5 pages
    result = first_5_pages
    return result

print(solution())