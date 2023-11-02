def solution():
    red_chairs = 5  # There are 5 red chairs
    yellow_chairs = 4 * red_chairs  # There are 4 times as many yellow chairs as red chairs
    blue_chairs = yellow_chairs - 2  # There are 2 fewer blue chairs than yellow chairs

    # Calculate the total number of chairs in Susan's house
    total_chairs = red_chairs + yellow_chairs + blue_chairs
    result = total_chairs
    return result

print(solution())