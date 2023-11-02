def solution():
    """Clara is selling boxes of cookies to raise money for a school trip. There are 3 different types for sale. The first type has 12 cookies per box. The second type has 20 cookies per box, and the third type has 16 cookies per box. If Clara sells 50 boxes of the first type, 80 boxes of the second type, and 70 boxes of the third type, how many cookies does she sell?"""
    # Define the number of cookies in each type of box
    TYPE1_COOKIES_PER_BOX = 12
    TYPE2_COOKIES_PER_BOX = 20
    TYPE3_COOKIES_PER_BOX = 16

    # Define the number of boxes sold of each type
    type1_boxes = 50
    type2_boxes = 80
    type3_boxes = 70

    # Calculate the total number of cookies sold
    total_cookies = (type1_boxes * TYPE1_COOKIES_PER_BOX) + (type2_boxes * TYPE2_COOKIES_PER_BOX) + (type3_boxes * TYPE3_COOKIES_PER_BOX)

    # Display the total number of cookies sold
    result = total_cookies
    return result

print(solution())