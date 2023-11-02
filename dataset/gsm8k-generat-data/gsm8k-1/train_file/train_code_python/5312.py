def solution():
    """Forest and his friends have prepared a birthday cake for their friend Juelz having 240 cake pieces. After singing the birthday song, they ate 60% of the cake's pieces, and later, Juelz divided the remaining pieces among his three sisters. What is the number of pieces of cake each sister received?"""
    total_pieces = 240
    eaten_percent = 60
    remaining_percent = 100 - eaten_percent
    remaining_pieces = total_pieces * (remaining_percent / 100)
    pieces_per_sister = remaining_pieces / 3
    result = pieces_per_sister
    return result

print(solution())