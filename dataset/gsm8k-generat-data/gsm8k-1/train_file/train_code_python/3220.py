def solution():
    """Kay has 14 siblings. Kay is 32 years old. The youngest sibling is 5 less than half Kay's age. The oldest sibling is four times as old as the youngest sibling. How old is the oldest sibling?"""
    num_siblings = 14
    kay_age = 32
    youngest_age = (kay_age / 2) - 5
    oldest_age = 4 * youngest_age
    total_siblings_age = (num_siblings - 1) * youngest_age + oldest_age + kay_age
    oldest_sibling_age = total_siblings_age - kay_age - (num_siblings - 2) * youngest_age
    result = oldest_sibling_age
    return result

print(solution())