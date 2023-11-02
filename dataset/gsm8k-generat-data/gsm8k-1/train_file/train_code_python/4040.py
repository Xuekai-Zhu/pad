def solution():
    """A boy has 12 oranges. He gives one-third of this number to his brother, one-fourth of the remainder to his friend and keeps the rest for himself. How many does his friend get?"""
    oranges = 12
    brother_share = oranges / 3
    remaining_oranges = oranges - brother_share
    friend_share = remaining_oranges / 4
    result = friend_share
    return result

print(solution())