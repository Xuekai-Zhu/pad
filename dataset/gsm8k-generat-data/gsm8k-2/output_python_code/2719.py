def solution():
    """Kaylee needs to sell 33 boxes of biscuits. So far, she has sold 12 boxes of lemon biscuits to her aunt, 5 boxes of chocolate biscuits to her mother, and 4 boxes of oatmeal biscuits to a neighbor. How many more boxes of biscuits does Kaylee need to sell?"""
    total_biscuits = 33
    sold_biscuits = 12 + 5 + 4
    remaining_biscuits = total_biscuits - sold_biscuits
    result = remaining_biscuits
    return result

print(solution())