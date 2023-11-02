def solution():
    """John has 10 members of his family on his father's side. His mother's side is 30% larger. How many people are there in total?"""
    father_members = 10
    mother_members = father_members * 1.3
    total_members = father_members + mother_members
    result = total_members
    return result

print(solution())