def solution():
    """Susan, Arthur, Tom and, Bob are siblings. Arthur is 2 years older than Susan, and Tom is 3 years younger than Bob. If Bob is 11 years old, and Susan is 15 years old, how old are all four family members in total?"""
    # Determine Arthur's age from Susan's age
    arthur_age = 15 + 2

    # Determine Tom's age from Bob's age
    tom_age = 11 - 3

    # Calculate the total age of all four siblings
    total_age = susan_age + arthur_age + bob_age + tom_age

    result = total_age
    return result

print(solution())