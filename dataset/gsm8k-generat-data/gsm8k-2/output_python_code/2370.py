def solution():
    """Tommy's mother lets him ride his bike 2 blocks north of his block, 3 blocks east, 2 blocks west, and 2 blocks south. His friend's father lets his friend ride his bike 80 square blocks. How many times greater is the area his friend can ride in compared to Tommy?"""
    tommy_area = (2 + 2) * (3 + 1) # 2 blocks north and 2 blocks south, 3 blocks east and 1 block west
    friend_area = 80
    times_greater = friend_area / tommy_area
    result = times_greater
    return result

print(solution())