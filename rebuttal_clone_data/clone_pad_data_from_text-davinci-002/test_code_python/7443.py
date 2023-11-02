def solution():
    harry_age = 50
    harry_fathers_age = harry_age + 24
    harry_mothers_age = harry_fathers_age - (harry_age / 25) -1
    result = harry_mothers_age
    return result

print(solution())