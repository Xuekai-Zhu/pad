def solution():
    # Let's assume Jeff has x trucks
    x = 0
    while True:
        # If he has twice as many cars as trucks, he has 2x cars
        # The total number of vehicles is 60
        if 2 * x + x == 60:
            result = x
            break
        # If the assumption is wrong, increment x and try again
        x += 1
    return result

print(solution())