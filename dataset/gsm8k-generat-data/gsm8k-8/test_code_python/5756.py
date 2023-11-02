def solution():
    # Define Nathan's writing speed
    nathan_speed = 25/1

    # Calculate Jacob's writing speed
    jacob_speed = 2 * nathan_speed

    # Calculate the total letters they can write together in one hour
    total_speed = nathan_speed + jacob_speed

    # Calculate the total letters they can write in 10 hours
    total_letters = total_speed * 10
    result = total_letters
    return result

print(solution())