def solution():
    # Calculate Nathan's writing speed
    nathan_speed = 25  # Nathan wrote 25 letters in 1 hour

    # Calculate Jacob's writing speed
    jacob_speed = 2 * nathan_speed  # Jacob can write twice as fast as Nathan

    # Calculate the total number of letters the two can write in 10 hours
    total_letters = (nathan_speed + jacob_speed) * 10

    result = total_letters
    return result

print(solution())