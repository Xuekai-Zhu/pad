def solution():
    """Ignatius owns 4 bicycles. A friend of his owns different types of cycles, which have three times are many tires as Ignatius's bikes have. He has one unicycle, a tricycle, and the rest are bikes. How many bicycles does the friend own?"""
    ig_bikes = 4
    friend_tires = ig_bikes * 3
    friend_uni = 1
    friend_tri = 1
    friend_bikes = (friend_tires - friend_uni*1 - friend_tri*3) / 2
    result = friend_bikes
    return result

print(solution())