def solution():
    """Frank has three less than half the number of cookies as Mike. Mike has three times as many cookies as Millie. If Millie has 4 cookies, how many cookies does Frank have?"""
    millie_cookies = 4
    mike_cookies = 3 * millie_cookies
    frank_cookies = (0.5 * mike_cookies) - 3
    result = frank_cookies
    return result

print(solution())