def solution():
    """For 5 days, Chantel makes 2 friendship bracelets every day. She gives away 3 bracelets to her friends at school. Then for four days, she makes 3 friendship bracelets every day. Then she gives away 6 bracelets to her friends at soccer practice. How many bracelets does Chantel have in the end?"""
    bracelets_made = (5 * 2) + (4 * 3)
    bracelets_given_away = 3 + 6
    total_bracelets = bracelets_made - bracelets_given_away
    result = total_bracelets
    return result

print(solution())