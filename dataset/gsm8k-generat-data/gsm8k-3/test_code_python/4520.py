def solution():
    """Cheryl has thrice as many colored pencils as Cyrus. Madeline has 63 colored pencils and only half of what Cheryl has. How many colored pencils do the three of them have altogether?"""
    # Let x be the number of colored pencils Cyrus has
    x = 21

    # Calculate the number of colored pencils Cheryl has
    cheryl = 3 * x

    # Calculate the total number of colored pencils
    total = x + cheryl + 63

    # Display the total number of colored pencils
    result = total
    return result

print(solution())