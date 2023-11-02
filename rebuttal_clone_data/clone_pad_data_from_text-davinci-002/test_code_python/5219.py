def solution():
    pieces = 60
    pieces_swept_up = pieces / 2
    pieces_stolen = 3
    pieces_remaining = pieces_swept_up - pieces_stolen
    pieces_picked_up = pieces_remaining / 3
    result = pieces_picked_up
    return result

print(solution())