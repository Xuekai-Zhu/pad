def solution():
    """Susan loves chairs. In her house there are red chairs, yellow chairs, and blue chairs. There are 5 red chairs. There are 4 times as many yellow chairs as red chairs, and there are 2 fewer blue chairs than yellow chairs. How many chairs are there in Susan's house?"""
    red_chairs = 5
    yellow_chairs = 4 * red_chairs
    blue_chairs = yellow_chairs - 2
    total_chairs = red_chairs + yellow_chairs + blue_chairs
    result = total_chairs
    return result

print(solution())