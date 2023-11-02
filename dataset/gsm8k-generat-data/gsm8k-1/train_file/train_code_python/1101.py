def solution():
    """To pass the time while she is waiting somewhere Carla likes to count things around her. While she is waiting for school to start on Monday she counts the tiles on the ceiling--38. While she is waiting for everyone to finish their tests after she has handed in hers, she counts the books in the room--75. On Tuesday Carla counts all the tiles twice in a row and she counts the books three times in a row when she has to wait for a long time for the teacher to finish handing out the graded tests. If every time Carla counts something counts as once, how many times has Carla counted something on Tuesday?"""
    tiles_on_monday = 38
    books_on_monday = 75
    tiles_on_tuesday = tiles_on_monday * 2
    books_on_tuesday = books_on_monday * 3
    total_count_on_tuesday = tiles_on_tuesday + books_on_tuesday
    result = total_count_on_tuesday
    return result

print(solution())