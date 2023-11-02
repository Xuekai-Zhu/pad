def solution():
    """Javier has a wife and 3 children. They have 2 dogs and 1 cat. Including Javier, how many legs are there in total in Javier’s household?"""
    javier_legs = 2
    wife_legs = 2
    children_legs = 3 * 2
    dogs_legs = 2 * 4
    cat_legs = 1 * 4
    total_legs = javier_legs + wife_legs + children_legs + dogs_legs + cat_legs
    result = total_legs
    return result

print(solution())