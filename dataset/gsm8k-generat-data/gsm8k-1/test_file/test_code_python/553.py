def solution():
    """A bag of buttons had 21 buttons in it. Seven buttons had two holes and the rest had four holes. How many holes were in all the buttons in the bag?"""
    total_buttons = 21
    two_hole_buttons = 7
    four_hole_buttons = total_buttons - two_hole_buttons
    total_holes = (2 * two_hole_buttons) + (4 * four_hole_buttons)
    result = total_holes
    return result

print(solution())