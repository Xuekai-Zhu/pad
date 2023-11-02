def solution():
    """To pass the time while she is waiting somewhere Carla likes to count things around her. While she is waiting for school to start on Monday she counts the tiles on the ceiling--38. While she is waiting for everyone to finish their tests after she has handed in hers, she counts the books in the room--75. On Tuesday Carla counts all the tiles twice in a row and she counts the books three times in a row when she has to wait for a long time for the teacher to finish handing out the graded tests. If every time Carla counts something counts as once, how many times has Carla counted something on Tuesday?"""
    # Define the number of tiles and books counted on Monday
    tiles_monday = 38
    books_monday = 75

    # Define the number of times the tiles and books are counted on Tuesday
    tiles_tuesday = 2
    books_tuesday = 3

    # Calculate the total number of times Carla counted something on Tuesday
    total_count = (tiles_monday * tiles_tuesday) + (books_monday * books_tuesday)

    result = total_count
    return result

print(solution())