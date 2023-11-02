def solution():
    """Susan, Arthur, Tom and, Bob are siblings. Arthur is 2 years older than Susan, and Tom is 3 years younger than Bob. If Bob is 11 years old, and Susan is 15 years old, how old are all four family members in total?"""
    susan_age = 15
    arthur_age = susan_age + 2
    bob_age = 11
    tom_age = bob_age - 3
    total_age = susan_age + arthur_age + bob_age + tom_age
    result = total_age
    return result

print(solution())