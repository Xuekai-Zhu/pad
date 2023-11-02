def solution():
    """TreShaun's full marker has enough ink in it to paint three 4 inch by 4 inch squares. If he colors in two 6 inch by 2 inch rectangles, what percentage of ink is left?"""
    # calculate the area of one 4 in x 4 in square
    one_square_area = 4 * 4

    # calculate the area of two 6 in x 2 in rectangles
    two_rectangles_area = 2 * 6 * 2

    # calculate the total area painted
    total_painted_area = two_rectangles_area

    # calculate the remaining ink area
    remaining_ink_area = (3 * one_square_area) - total_painted_area

    # calculate the percentage of ink remaining
    percent_ink_remaining = (remaining_ink_area / (3 * one_square_area)) * 100

    # display the percentage of ink remaining
    result = percent_ink_remaining
    return result

print(solution())