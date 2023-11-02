def solution():
    legal_drinking_age = 21
    millie_bobby_brown_age = 16
    if millie_bobby_brown_age < legal_drinking_age:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())