def solution():
    """Tom plants a tree that is 1 year old and 5 feet tall. It gains 3 feet per year. How old is it when it is 23 feet tall?"""
    initial_height = 5
    growth_rate = 3
    target_height = 23
    age = 0
    while initial_height < target_height:
        initial_height += growth_rate
        age += 1
    result = age + 1  # add 1 to account for the initial year
    return result

print(solution())