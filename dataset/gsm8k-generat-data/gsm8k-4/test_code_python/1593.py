def solution():
    """Yun had 20 paperclips initially, but then lost 12. Marion has 1/4 more than what Yun currently has, plus 7. How many paperclips does Marion have?"""
    # Define the initial number of paperclips Yun had
    yun_paperclips = 20

    # Calculate the number of paperclips Yun has now
    yun_paperclips_now = yun_paperclips - 12

    # Calculate the number of paperclips Marion has
    marion_paperclips = yun_paperclips_now * 1.25 + 7

    # Return the result
    result = marion_paperclips
    return result

print(solution())