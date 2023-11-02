def solution():
    """In a fruit salad, there are raspberries, green grapes, and red grapes. There are seven more than 3 times the number of red grapes as green grapes. There are 5 less raspberries than green grapes. If there are 102 pieces of fruit in the salad, how many red grapes are in the salad?"""
    # Let's assume number of green grapes = g
    g = 20 # We can start with any number as it is not provided in the question
    r = 7 + 3*g
    b = g - 5
    total_fruits = r + g + b

    while total_fruits != 102:
        if total_fruits < 102:
            g += 1
        else:
            g -= 1

        r = 7 + 3*g
        b = g - 5
        total_fruits = r + g + b

    result = r
    return result

print(solution())