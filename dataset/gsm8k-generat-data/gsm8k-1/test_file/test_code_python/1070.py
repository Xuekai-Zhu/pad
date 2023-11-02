def solution():
    """Teddy finished half of a 500 piece puzzle, and then started and finished another 500 piece puzzle within an hour. How many puzzle pieces did Teddy place during that hour?"""
    completed_pieces = 500
    total_pieces = (completed_pieces / 2) + completed_pieces
    result = total_pieces
    return result

print(solution())