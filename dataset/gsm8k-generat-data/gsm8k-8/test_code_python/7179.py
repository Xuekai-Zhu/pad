def solution():
    # Calculate the total number of each colored marble in each basket
    a_red = 4
    a_yellow = 2
    b_green = 6
    b_yellow = 1
    c_white = 3
    c_yellow = 9

    # Calculate the difference in the number of each colored marble in each basket
    diff_a = abs(a_red - a_yellow)
    diff_b = abs(b_green - b_yellow)
    diff_c = abs(c_white - c_yellow)

    # Find the maximum difference among the three baskets
    max_diff = max(diff_a, diff_b, diff_c)
    
    result = max_diff
    return result

print(solution())