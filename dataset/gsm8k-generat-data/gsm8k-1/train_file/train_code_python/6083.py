def solution():
    """There are 15 girls and 10 boys in Ms. Smith's class. She divided 375 books equally among them. How many books did all the girls get combined?"""
    total_students = 15 + 10
    girls_share = (15 / total_students) * 375
    result = girls_share
    return result

print(solution())