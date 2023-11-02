def solution():
    
    name_length = len("Sarah")
    age = 9
    marriage_age = (name_length + (2 * age)) % 50
    result = marriage_age
    return result

print(solution())