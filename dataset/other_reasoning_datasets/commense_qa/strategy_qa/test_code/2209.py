def solution():
    current_age = 65
    legal_drinking_age = 21
    if current_age < legal_drinking_age:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())