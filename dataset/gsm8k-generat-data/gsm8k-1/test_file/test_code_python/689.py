def solution():
    """Brittany's quilted comforter has many 1-foot by 1-foot colored squares. The comforter had 14 red squares, 4 more blue squares than red squares, 6 more green squares than blue squares, and 12 fewer white squares than green squares. How many square feet is Brittany's comforter?"""
    red_squares = 14
    blue_squares = red_squares + 4
    green_squares = blue_squares + 6
    white_squares = green_squares - 12
    total_squares = red_squares + blue_squares + green_squares + white_squares
    square_feet = total_squares * 1 * 1
    result = square_feet
    return result

print(solution())