def solution():
    """Markus is twice the age of his son, and Markus's son is twice the age of Markus's grandson. If the sum of the ages of Markus, his son, and his grandson is 140 years, then how many years old is Markus's grandson?"""
    total_age = 140
    grandson_age = total_age / 7
    son_age = grandson_age * 2
    markus_age = son_age * 2
    result = grandson_age
    return result

print(solution())