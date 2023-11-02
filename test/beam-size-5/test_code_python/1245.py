def solution():
    num_rooms = 8
    num_people = 4
    num_flashlights = 2 * num_people

    num_small_rooms = num_rooms // 2
    num_medium_rooms = num_rooms // 2

    num_small_candles = num_small_rooms * 4
    num_medium_candles = num_medium_rooms * 5

    total_candles = num_rooms * num_small_candles + num_medium_candles + num_flashlights
    result = total_candles
    return result

print(solution())