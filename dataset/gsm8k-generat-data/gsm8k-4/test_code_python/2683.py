def solution():
    """Alexandra bought 8 magazines at the bookstore on Friday. On Saturday, she went back and bought 12 more. Sunday morning, she saw that the store was having a sale and she bought four times the number of magazines she did on Friday. Later that day she discovered that her dog had chewed up 4 of the magazines. How many magazines does she have now?"""
    # Calculate the total number of magazines purchased before the sale
    total_magazines = 8 + 12

    # Calculate the number of magazines purchased on Sunday
    sunday_magazines = 4 * 8

    # Add the Sunday magazines to the total magazines and subtract the chewed up ones
    total_magazines = total_magazines + sunday_magazines - 4

    result = total_magazines
    return result

print(solution())