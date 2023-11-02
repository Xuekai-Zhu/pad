def solution():
    
    buttons_in_bag = 21
    buttons_with_two_holes = 7
    buttons_with_four_holes = buttons_in_bag - buttons_with_two_holes
    total_holes = buttons_with_two_holes + buttons_with_four_holes
    result = total_holes
    return result

print(solution())