def solution():
    """Elon has 10 more teslas than Sam who has half the number of teslas as Chris. Chris has 6 teslas. How many teslas does Elon have?"""
    # Define the number of teslas Chris has
    chris_teslas = 6

    # Calculate the number of teslas Sam has
    sam_teslas = chris_teslas // 2

    # Calculate the number of teslas Elon has
    elon_teslas = sam_teslas + 10

    # Display the number of teslas Elon has
    result = elon_teslas
    return result

print(solution())