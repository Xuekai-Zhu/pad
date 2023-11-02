def solution():
    """It’s February 2021. Mark was born in January 1976. Graham is 3 years younger than Mark, and Graham’s sister, Janice, is 1/2 the age of Graham. How old is Janice?"""
    mark_age = 2021 - 1976
    graham_age = mark_age - 3
    janice_age = graham_age / 2
    result = janice_age
    return result

print(solution())