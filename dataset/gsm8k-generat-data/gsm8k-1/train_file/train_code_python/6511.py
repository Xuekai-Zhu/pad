def solution():
    """Clara is selling boxes of cookies to raise money for a school trip. There are 3 different types for sale. The first type has 12 cookies per box. The second type has 20 cookies per box, and the third type has 16 cookies per box. If Clara sells 50 boxes of the first type, 80 boxes of the second type, and 70 boxes of the third type, how many cookies does she sell?"""
    cookies_per_box1 = 12
    cookies_per_box2 = 20
    cookies_per_box3 = 16
    num_boxes1 = 50
    num_boxes2 = 80
    num_boxes3 = 70
    total_cookies = (cookies_per_box1 * num_boxes1) + (cookies_per_box2 * num_boxes2) + (cookies_per_box3 * num_boxes3)
    result = total_cookies
    return result

print(solution())