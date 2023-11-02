def solution():
    
    # Define the thickness of the first book
    book1_thickness = 31

    # Define the thickness of the second book
    book2_thickness = 50

    # Define the thickness of the third book
    book3_thickness = book2_thickness - 5

    # Define the thickness of the fourth book
    book4_thickness = book1_thickness * 2

    # Calculate the total thickness of the four books
    total_thickness = book1_thickness + book2_thickness + book3_thickness + book4_thickness

    # Display the total thickness
    result = total_thickness
    return result

print(solution())