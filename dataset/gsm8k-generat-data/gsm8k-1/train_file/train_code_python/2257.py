def solution():
    """Dan has two times as many stickers as Tom. Tom has 3 times as many stickers as Bob. If Bob has 12 stickers, how many does Dan have?"""
    bob_stickers = 12
    tom_stickers = bob_stickers * 3
    dan_stickers = tom_stickers * 2
    result = dan_stickers
    return result

print(solution())