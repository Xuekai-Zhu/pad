def solution():
    """After Bella’s ballet performance, she received 2 dozen roses from her parents, and 2 roses from each of her 10 dancer friends. How many roses did Bella receive?"""
    dozen_roses = 2
    parent_roses = dozen_roses * 12 * 2
    friend_roses = 2 * 10
    total_roses = parent_roses + friend_roses
    result = total_roses
    return result

print(solution())