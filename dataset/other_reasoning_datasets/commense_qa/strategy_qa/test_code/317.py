def solution():
    common_intellectual_disabilities = ["Intellectual disability"]
    dyslexia = "Dyslexia"
    successful presidents_with dyslexia = ["Thomas Jefferson", "George Washington", "John F. Kennedy"]
    if dyslexia in common_intellectual_disabilities and successful presidents_with dyslexia:
        result = "no"
    else:
        result = "not enough information"
    return result

print(solution())