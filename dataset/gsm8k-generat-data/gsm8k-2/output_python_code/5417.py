def solution():
    """There are 480 zombies in the shopping mall. If the number of zombies doubled every day, how many days ago were there less than 50 zombies in the mall?"""
    zombie_count = 480
    days_ago = 0
    while zombie_count >= 50:
        zombie_count /= 2
        days_ago += 1
    result = days_ago
    return result

print(solution())