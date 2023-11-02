def solution():
    """Jacob can write twice as fast as Nathan. Nathan wrote 25 letters in one hour. How many letters can the two write in 10 hours together?"""
    # Determine Nathan's writing speed
    nathan_speed = 25

    # Determine Jacob's writing speed
    jacob_speed = nathan_speed * 2

    # Determine how many letters they can write together in one hour
    combined_speed = nathan_speed + jacob_speed

    # Determine how many letters they can write together in 10 hours
    letters_in_10_hours = combined_speed * 10

    result = letters_in_10_hours
    return result

print(solution())