def solution():
    """For 5 days, Chantel makes 2 friendship bracelets every day. She gives away 3 bracelets to her friends at school. Then for four days, she makes 3 friendship bracelets every day. Then she gives away 6 bracelets to her friends at soccer practice. How many bracelets does Chantel have in the end?"""
    # Calculate the number of bracelets made in the first 5 days
    bracelets1 = 5 * 2

    # Calculate the number of bracelets remaining after giving away 3 at school
    bracelets1 -= 3

    # Calculate the number of bracelets made in the next 4 days
    bracelets2 = 4 * 3

    # Calculate the number of bracelets remaining after giving away 6 at soccer practice
    bracelets2 -= 6

    # Calculate the total number of bracelets Chantel has
    total_bracelets = bracelets1 + bracelets2

    # Display the total number of bracelets
    result = total_bracelets
    return result

print(solution())