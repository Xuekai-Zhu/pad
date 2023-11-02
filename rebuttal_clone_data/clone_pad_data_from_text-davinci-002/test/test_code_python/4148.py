def solution():
    blue_rectangle_inches = 6 * 7
    red_square_inches = 5 * 5
    total_square_inches = blue_rectangle_inches + red_square_inches
    grams_per_square_inch = 3
    total_grams = total_square_inches * grams_per_square_inch
    result = total_grams
    return result

print(solution())