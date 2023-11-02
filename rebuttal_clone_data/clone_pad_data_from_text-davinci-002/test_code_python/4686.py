def solution():
    shirts_washed = 20
    shorts_washed = 8
    shirts_folded = 12
    shorts_folded = 5
    shirts_remaining = shirts_washed - shirts_folded
    shorts_remaining = shorts_washed - shorts_folded
    items_remaining = shirts_remaining + shorts_remaining
    result = items_remaining
    return result

print(solution())