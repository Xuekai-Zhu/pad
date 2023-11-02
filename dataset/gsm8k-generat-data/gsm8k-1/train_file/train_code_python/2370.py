def solution():
    """Tommy's mother lets him ride his bike 2 blocks north of his block, 3 blocks east, 2 blocks west, and 2 blocks south. His friend's father lets his friend ride his bike 80 square blocks. How many times greater is the area his friend can ride in compared to Tommy?"""
    tommy_blocks = 2 + 2 + 3 + 2
    tommy_area = tommy_blocks ** 2
    friend_area = 80
    ratio = friend_area / tommy_area
    result = ratio
    return result

print(solution())