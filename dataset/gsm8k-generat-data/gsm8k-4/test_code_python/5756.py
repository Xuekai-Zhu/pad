def solution():
    """Jacob can write twice as fast as Nathan. Nathan wrote 25 letters in one hour. How many letters can the two write in 10 hours together?"""
    # Define Nathan's writing speed
    nathan_speed = 25 / 1  # 25 letters in 1 hour

    # Define Jacob's writing speed
    jacob_speed = 2 * nathan_speed

    # Calculate the total number of letters they can write together in 1 hour
    total_speed = nathan_speed + jacob_speed

    # Calculate the total number of letters they can write together in 10 hours
    total_letters = total_speed * 10

    # return the result
    result = total_letters
    return result

print(solution())