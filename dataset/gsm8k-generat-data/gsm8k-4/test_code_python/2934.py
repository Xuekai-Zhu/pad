def solution():
    """Mary only has 8 screws on hand and needs to buy 2 times more to fix her sink. When she is beginning repairs, she has to split the screws into four sections. How many are in each pile?"""
    # Calculate the total number of screws needed
    total_screws = 8 * 3

    # Calculate the number of screws in each pile
    screws_per_pile = total_screws / 4

    # Return the result
    result = screws_per_pile
    return result

print(solution())