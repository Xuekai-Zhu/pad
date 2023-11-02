def solution():
    """Elon has 10 more teslas than Sam who has half the number of teslas as Chris. Chris has 6 teslas. How many teslas does Elon have?"""
    chris_teslas = 6
    sam_teslas = chris_teslas / 2
    elon_teslas = sam_teslas + 10
    result = elon_teslas
    return result

print(solution())