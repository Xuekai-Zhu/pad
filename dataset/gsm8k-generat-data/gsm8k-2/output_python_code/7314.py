def solution():
    """After Bella’s ballet performance, she received 2 dozen roses from her parents, and 2 roses from each of her 10 dancer friends. How many roses did Bella receive?"""
    dozen_of_roses = 2
    roses_from_parents = dozen_of_roses * 12 * 2
    roses_from_friends = 2 * 10
    total_roses = roses_from_parents + roses_from_friends
    result = total_roses
    return result

print(solution())