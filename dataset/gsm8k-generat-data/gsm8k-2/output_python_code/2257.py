def solution():
    """Dan has two times as many stickers as Tom. Tom has 3 times as many stickers as Bob. If Bob has 12 stickers, how many does Dan have?"""
    bob_stickers = 12
    tom_stickers = 3 * bob_stickers
    dan_stickers = 2 * tom_stickers
    result = dan_stickers
    return result

print(solution())