def solution():
    """TreShaun's full marker has enough ink in it to paint three 4 inch by 4 inch squares. If he colors in two 6 inch by 2 inch rectangles, what percentage of ink is left?"""
    # Define the area of one 4x4 square
    square_area = 4 * 4

    # Calculate the total ink available
    total_ink = square_area * 3

    # Calculate the ink used to color the two 6x2 rectangles
    rectangle_ink = 6 * 2 * 2

    # Calculate the remaining ink percentage
    remaining_ink_percentage = ((total_ink - rectangle_ink) / total_ink) * 100

    # return the result
    result = remaining_ink_percentage
    return result

print(solution())