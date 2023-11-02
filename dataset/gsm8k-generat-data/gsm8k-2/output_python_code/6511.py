def solution():
    """Clara is selling boxes of cookies to raise money for a school trip. There are 3 different types for sale. The first type has 12 cookies per box. The second type has 20 cookies per box, and the third type has 16 cookies per box. If Clara sells 50 boxes of the first type, 80 boxes of the second type, and 70 boxes of the third type, how many cookies does she sell?"""
    first_type_cookies = 12 * 50
    second_type_cookies = 20 * 80
    third_type_cookies = 16 * 70
    total_cookies = first_type_cookies + second_type_cookies + third_type_cookies
    result = total_cookies
    return result

print(solution())