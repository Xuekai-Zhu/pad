def solution():
    """Cheryl has thrice as many colored pencils as Cyrus. Madeline has 63 colored pencils and only half of what Cheryl has. How many colored pencils do the three of them have altogether?"""
    # Define the initial number of colored pencils
    cheryl_pencils = None
    cyrus_pencils = None

    # Calculate the number of colored pencils Madeline has
    madeline_pencils = 63

    # Calculate the number of pencils Cheryl has
    cheryl_pencils = madeline_pencils * 2

    # Calculate the number of pencils Cyrus has
    cyrus_pencils = cheryl_pencils / 3

    # Calculate the total number of pencils
    total_pencils = cheryl_pencils + cyrus_pencils + madeline_pencils

    # return the result
    result = total_pencils
    return result

print(solution())