def solution():
    """Clara is selling boxes of cookies to raise money for a school trip. There are 3 different types for sale. The first type has 12 cookies per box. The second type has 20 cookies per box, and the third type has 16 cookies per box. If Clara sells 50 boxes of the first type, 80 boxes of the second type, and 70 boxes of the third type, how many cookies does she sell?"""
    # Define the number of boxes sold for each type of cookie
    type1_boxes = 50
    type2_boxes = 80
    type3_boxes = 70

    # Define the number of cookies per box for each type of cookie
    type1_cookies = 12
    type2_cookies = 20
    type3_cookies = 16

    # Calculate the total number of cookies sold
    total_cookies = type1_boxes * type1_cookies + type2_boxes * type2_cookies + type3_boxes * type3_cookies

    # return the result
    result = total_cookies
    return result

print(solution())