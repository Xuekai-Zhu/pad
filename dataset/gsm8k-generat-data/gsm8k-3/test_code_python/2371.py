def solution():
    """Tommy's mother lets him ride his bike 2 blocks north of his block, 3 blocks east, 2 blocks west, and 2 blocks south. His friend's father lets his friend ride his bike 80 square blocks. How many times greater is the area his friend can ride in compared to Tommy?"""
    # Define the area Tommy can ride in
    tommy_area = (2 + 2) * (3 + 1) - 2 * 2

    # Define the area Tommy's friend can ride in
    friend_area = 80

    # Calculate how many times greater the friend's riding area is compared to Tommy's
    times_greater = friend_area / tommy_area

    # Round to two decimal places
    result = round(times_greater, 2)
    return result

print(solution())