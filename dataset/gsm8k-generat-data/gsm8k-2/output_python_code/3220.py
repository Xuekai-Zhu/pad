def solution():
    """Kay has 14 siblings. Kay is 32 years old. The youngest sibling is 5 less than half Kay's age. The oldest sibling is four times as old as the youngest sibling. How old is the oldest sibling?"""
    total_siblings = 14
    kay_age = 32
    youngest_sibling_age = (kay_age / 2) - 5
    oldest_sibling_age = 4 * youngest_sibling_age
    for i in range(total_siblings):
        if i == 0:
            age_list = [youngest_sibling_age]
        else:
            age_list.append(age_list[-1] + 2)
    age_list.sort()
    result = age_list[-1] + oldest_sibling_age
    return result

print(solution())