def solution():
    border_pieces = 75
    Trevor_pieces = 105
    Joe_pieces = Trevor_pieces * 3
    total_pieces = border_pieces + Trevor_pieces + Joe_pieces
    missing_pieces = 500 - total_pieces
    result = missing_pieces

print(solution())