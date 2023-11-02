def solution():
    """For 5 days, Chantel makes 2 friendship bracelets every day. She gives away 3 bracelets to her friends at school. Then for four days, she makes 3 friendship bracelets every day. Then she gives away 6 bracelets to her friends at soccer practice. How many bracelets does Chantel have in the end?"""
    initial_bracelets = 0
    for i in range(5):
        initial_bracelets += 2
    initial_bracelets -= 3 # Giving away 3 bracelets at school
    for i in range(4):
        initial_bracelets += 3
    initial_bracelets -= 6 # Giving away 6 bracelets at soccer practice
    result = initial_bracelets
    return result

print(solution())