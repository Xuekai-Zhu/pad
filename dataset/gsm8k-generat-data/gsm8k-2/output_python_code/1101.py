def solution():
    """To pass the time while she is waiting somewhere Carla likes to count things around her. While she is waiting for school to start on Monday she counts the tiles on the ceiling--38. While she is waiting for everyone to finish their tests after she has handed in hers, she counts the books in the room--75. On Tuesday Carla counts all the tiles twice in a row and she counts the books three times in a row when she has to wait for a long time for the teacher to finish handing out the graded tests. If every time Carla counts something counts as once, how many times has Carla counted something on Tuesday?"""
    monday_tiles_count = 38
    monday_books_count = 75
    tuesday_tiles_count = 2 * monday_tiles_count
    tuesday_books_count = 3 * monday_books_count
    total_count = tuesday_tiles_count + tuesday_books_count
    result = total_count
    return result

print(solution())