def solution():
    """Jacob can write twice as fast as Nathan. Nathan wrote 25 letters in one hour. How many letters can the two write in 10 hours together?"""
    nathan_speed = 25 # letters per hour
    jacob_speed = 2 * nathan_speed # letters per hour
    total_speed = nathan_speed + jacob_speed # letters per hour
    hours = 10
    total_letters = total_speed * hours
    result = total_letters
    return result

print(solution())