def solution():
    """Mr. Smith had 32 markers in his classroom. He buys new boxes of markers that have 9 markers in each box. Now, he has 86 markers. How many new boxes did Mr. Smith buy?"""
    # Define the initial number of markers and the markers per box
    initial_markers = 32
    markers_per_box = 9

    # Calculate the number of new markers and boxes
    new_markers = 86 - initial_markers
    new_boxes = new_markers // markers_per_box

    # Return the result
    result = new_boxes
    return result

print(solution())