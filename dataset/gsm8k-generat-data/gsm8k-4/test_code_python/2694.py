def solution():
    """Frank has three less than half the number of cookies as Mike. Mike has three times as many cookies as Millie. If Millie has 4 cookies, how many cookies does Frank have?"""
    # Define the number of cookies Millie has
    millie_cookies = 4

    # Calculate the number of cookies Mike has
    mike_cookies = millie_cookies * 3

    # Calculate the number of cookies Frank has
    frank_cookies = (mike_cookies / 2) - 3

    # Return the result
    result = frank_cookies
    return result

print(solution())