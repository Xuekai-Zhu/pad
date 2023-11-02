def solution():
    nathan_speed = 25/1  # Nathan's speed in letters per hour
    jacob_speed = nathan_speed * 2  # Jacob's speed in letters per hour
    total_time = 10  # Total time in hours
    nathan_letters = nathan_speed * total_time
    jacob_letters = jacob_speed * total_time
    total_letters = nathan_letters + jacob_letters
    result = total_letters
    return result

print(solution())