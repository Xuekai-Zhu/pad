def solution():
    """Jacob can write twice as fast as Nathan. Nathan wrote 25 letters in one hour. How many letters can the two write in 10 hours together?"""
    nathan_speed = 25
    jacob_speed = 2 * nathan_speed
    nathan_letters = nathan_speed * 10
    jacob_letters = jacob_speed * 10
    total_letters = nathan_letters + jacob_letters
    result = total_letters
    return result

print(solution())