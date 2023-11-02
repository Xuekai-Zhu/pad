def solution():
    """Mary has 400 sheep on her farm. She gave a quarter of her sheep to her sister, and half of the remaining sheep to her brother. How many sheep remain with Mary?"""
    starting_sheep = 400
    sheep_given_to_sister = starting_sheep / 4
    remaining_sheep = starting_sheep - sheep_given_to_sister
    sheep_given_to_brother = remaining_sheep / 2
    sheep_remaining = remaining_sheep - sheep_given_to_brother
    result = sheep_remaining
    return result

print(solution())