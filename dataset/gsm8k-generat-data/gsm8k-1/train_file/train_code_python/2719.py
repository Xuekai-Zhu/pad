def solution():
    """Kaylee needs to sell 33 boxes of biscuits. So far, she has sold 12 boxes of lemon biscuits to her aunt, 5 boxes of chocolate biscuits to her mother, and 4 boxes of oatmeal biscuits to a neighbor. How many more boxes of biscuits does Kaylee need to sell?"""
    total_boxes = 33
    sold_boxes = 12 + 5 + 4
    remaining_boxes = total_boxes - sold_boxes
    result = remaining_boxes
    return result

print(solution())