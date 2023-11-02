def solution():
    """Dan has two times as many stickers as Tom. Tom has 3 times as many stickers as Bob. If Bob has 12 stickers, how many does Dan have?"""
    # Define the initial number of stickers Bob has
    bob_stickers = 12

    # Calculate the number of stickers Tom has
    tom_stickers = bob_stickers * 3

    # Calculate the number of stickers Dan has
    dan_stickers = tom_stickers * 2

    # return the result
    result = dan_stickers
    return result

print(solution())