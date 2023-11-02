def solution():
    """Lily bought a Russian nesting doll as a souvenir. The biggest doll is 243 cm tall, and each doll is 2/3rd the size of the doll that contains it. How big is the 6th biggest doll?"""
    biggest_doll_size = 243
    sixth_doll_size = biggest_doll_size * (2/3) ** 5
    result = sixth_doll_size
    return result

print(solution())