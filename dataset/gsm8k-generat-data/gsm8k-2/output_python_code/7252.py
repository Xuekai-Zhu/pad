def solution():
    """In Rodrigo's classroom in the morning there are red chairs, yellow chairs, and blue chairs. There are 4 red chairs.
    There are 2 times as many yellow chairs as red chairs, and there are 2 fewer blue chairs than yellow chairs.
    In the afternoon, Lisa borrows 3 chairs. How many chairs are left in Rodrigo's classroom?"""
    red_chairs = 4
    yellow_chairs = 2 * red_chairs
    blue_chairs = yellow_chairs - 2
    total_chairs = red_chairs + yellow_chairs + blue_chairs
    borrowed_chairs = 3
    chairs_left = total_chairs - borrowed_chairs
    result = chairs_left
    return result

print(solution())