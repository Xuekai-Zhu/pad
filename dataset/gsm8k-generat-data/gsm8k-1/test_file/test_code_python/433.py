def solution():
    """Sitti and Juris bought 34 and 22 oranges, respectively. If both of them decide to share them equally with their 6 other friends, how many oranges will everyone get?"""
    sitti_oranges = 34
    juris_oranges = 22
    total_oranges = sitti_oranges + juris_oranges
    total_friends = 6 + 2  # Sitti and Juris
    oranges_per_person = total_oranges // total_friends
    result = oranges_per_person
    return result

print(solution())