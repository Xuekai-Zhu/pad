def solution():
    """Alexandra bought 8 magazines at the bookstore on Friday. On Saturday, she went back and bought 12 more. Sunday morning, she saw that the store was having a sale and she bought four times the number of magazines she did on Friday. Later that day she discovered that her dog had chewed up 4 of the magazines. How many magazines does she have now?"""
    friday_magazines = 8
    saturday_magazines = 12
    sunday_magazines = 4 * friday_magazines
    total_magazines = friday_magazines + saturday_magazines + sunday_magazines - 4
    result = total_magazines
    return result

print(solution())