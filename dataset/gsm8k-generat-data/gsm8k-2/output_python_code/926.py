def solution():
    """Ashley had a birthday party and invited 20 of her friends, telling them to each invite one more person to attend the party. If half the number of the invited guests each came with one more person, what's the total number of people at the party, including Ashley?"""
    initial_guests = 20
    additional_guests = initial_guests * 0.5
    total_guests = initial_guests + additional_guests
    result = total_guests + 1  # add 1 for Ashley
    return result

print(solution())