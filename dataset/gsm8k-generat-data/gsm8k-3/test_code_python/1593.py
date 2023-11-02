def solution():
    """Yun had 20 paperclips initially, but then lost 12. Marion has 1/4 more than what Yun currently has, plus 7. How many paperclips does Marion have?"""
    # Calculate the number of paperclips Yun currently has
    yun_paperclips = 20 - 12

    # Calculate the number of paperclips Marion has
    marion_paperclips = int(yun_paperclips * 1.25) + 7

    # Display the number of paperclips Marion has
    result = marion_paperclips
    return result

print(solution())