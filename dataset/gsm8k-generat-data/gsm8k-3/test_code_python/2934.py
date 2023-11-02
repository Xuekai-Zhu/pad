def solution():
    """Mary only has 8 screws on hand and needs to buy 2 times more to fix her sink. When she is beginning repairs, she has to split the screws into four sections. How many are in each pile?"""
    # Mary needs to buy 2 times more screws than what she has
    total_screws = 8 * 3

    # The screws need to be split into 4 equal sections
    screws_per_pile = total_screws / 4

    # Display the number of screws in each pile
    result = screws_per_pile
    return result

print(solution())