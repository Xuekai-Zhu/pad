def solution():
    # Define the number of boxes sold for each type
    type1_boxes = 50
    type2_boxes = 80
    type3_boxes = 70

    # Define the number of cookies per box for each type
    type1_cookies = 12
    type2_cookies = 20
    type3_cookies = 16

    # Calculate the total number of cookies sold
    total_cookies = (type1_boxes * type1_cookies) + (type2_boxes * type2_cookies) + (type3_boxes * type3_cookies)
    
    result = total_cookies
    return result

print(solution())