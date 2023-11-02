def solution():
    """Lou Senior took 3 cookies out of the cookie jar and ate them. Since he didn't get caught by his wife, he went back the next day and took another 3 cookies out of the jar. But after eating just one of the cookies, he felt guilty about it and put the other two cookies back. His son, Louie Junior saw that his Dad was eating cookies. So, Louie Junior took seven cookies out of the jar and hid them in his bedroom for later. The next morning, Debra, Lou's wife looked into the cookie jar and reacted by accusing her husband of eating half of the cookies out of the cookie jar. How many cookies remained in the jar?"""
    # Define the initial number of cookies in the jar
    initial_cookies = None

    # Lou Senior took 3 cookies out of the jar
    initial_cookies = initial_cookies + 3

    # Lou Senior took 3 more cookies out of the jar
    initial_cookies = initial_cookies + 3

    # Lou Senior put 2 cookies back in the jar
    initial_cookies = initial_cookies + 2

    # Louie Junior took 7 cookies out of the jar
    initial_cookies = initial_cookies - 7

    # Debra accused Lou Senior of eating half of the cookies, so we can solve for the initial number of cookies using:
    # initial_cookies / 2 = remaining_cookies
    remaining_cookies = initial_cookies / 2

    result = remaining_cookies
    return result

print(solution())