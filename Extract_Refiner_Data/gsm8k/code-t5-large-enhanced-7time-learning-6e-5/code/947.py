def solution():
    
    # Define the number of pages in the book
    pages_per_inch = 100

    # Define the thickness of the book in inches
    thickness = 1.5

    # Calculate the number of pages printed on both sides of the book
    pages_per_side = pages_per_inch / 2

    # Calculate the total number of pages in the book
    total_pages = pages_per_side * thickness

    # return the result
    result = total_pages
    return result

print(solution())