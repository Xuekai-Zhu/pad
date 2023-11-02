def solution():
    """The power goes out in Brianna's house one night so she and her family gather all their candles and flashlights. There are 8 rooms in the house and 4 people living there, including Brianna. There is a flashlight for every person to carry and two for each room. They have a variety of candles available; 4 small candles each for half the rooms and 5 medium candles each for the other half of the rooms. With everything combined, how many candles and flashlights are Brianna's family using when the lights go out?"""
    num_rooms = 8
    num_people = 4
    flashlights = num_people + (num_rooms * 2)
    num_half_rooms = num_rooms // 2
    small_candles = num_half_rooms * 4
    medium_candles = (num_rooms - num_half_rooms) * 5
    total_candles = small_candles + medium_candles
    result = flashlights + total_candles
    return result

print(solution())