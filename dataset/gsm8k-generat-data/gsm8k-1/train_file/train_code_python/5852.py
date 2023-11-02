def solution():
    """In a fruit salad, there are raspberries, green grapes, and red grapes. There are seven more than 3 times the number of red grapes as green grapes. There are 5 less raspberries than green grapes. If there are 102 pieces of fruit in the salad, how many red grapes are in the salad?"""
    total_fruit = 102
    green_grapes = x
    red_grapes = 3 * green_grapes + 7
    raspberries = green_grapes - 5
    total_grapes = green_grapes + red_grapes
    total_pieces = raspberries + total_grapes
    red_grapes = (total_fruit - raspberries - total_grapes) / 3
    result = red_grapes
    return result

print(solution())