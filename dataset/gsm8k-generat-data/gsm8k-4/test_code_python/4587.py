def solution():
    """For 5 days, Chantel makes 2 friendship bracelets every day. She gives away 3 bracelets to her friends at school. Then for four days, she makes 3 friendship bracelets every day. Then she gives away 6 bracelets to her friends at soccer practice. How many bracelets does Chantel have in the end?"""
    # Calculate the number of bracelets Chantel makes and keeps for the first 5 days
    bracelets_first_five = 2 * 5

    # Calculate the number of bracelets Chantel gives away at school
    bracelets_given_school = 3

    # Calculate the number of bracelets Chantel makes and keeps for the next 4 days
    bracelets_next_four = 3 * 4

    # Calculate the number of bracelets Chantel gives away at soccer practice
    bracelets_given_soccer = 6

    # Calculate the total number of bracelets Chantel has in the end
    total_bracelets = (bracelets_first_five - bracelets_given_school) + (bracelets_next_four - bracelets_given_soccer)

    result = total_bracelets
    return result

print(solution())