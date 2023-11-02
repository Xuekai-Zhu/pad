def solution():
    """Mary only has 8 screws on hand and needs to buy 2 times more to fix her sink. When she is beginning repairs, she has to split the screws into four sections. How many are in each pile?"""
    initial_screws = 8
    needed_screws = initial_screws * 2
    piles = 4
    screws_per_pile = needed_screws / piles
    result = screws_per_pile
    return result

print(solution())