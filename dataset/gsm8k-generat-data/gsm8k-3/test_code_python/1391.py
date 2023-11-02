def solution():
    """Susan, Arthur, Tom and, Bob are siblings. Arthur is 2 years older than Susan, and Tom is 3 years younger than Bob. If Bob is 11 years old, and Susan is 15 years old, how old are all four family members in total?"""
    # Calculate Arthur's age
    arthur_age = 15 + 2

    # Calculate Tom's age
    tom_age = 11 - 3

    # Calculate the total age of all four siblings
    total_age = 15 + arthur_age + tom_age + 11

    # Display the total age
    result = total_age
    return result

print(solution())