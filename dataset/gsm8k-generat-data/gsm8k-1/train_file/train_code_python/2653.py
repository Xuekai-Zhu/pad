def solution():
    """Jack bought 55 apples. He wants to give 10 to his father and then equally share the remaining apples between him and his 4 friends. How many apples will each of them get?"""
    total_apples = 55
    apples_given_away = 10
    apples_remaining = total_apples - apples_given_away
    friends = 4
    apples_per_person = apples_remaining / (friends + 1) # Adding 1 for himself
    result = apples_per_person
    return result

print(solution())