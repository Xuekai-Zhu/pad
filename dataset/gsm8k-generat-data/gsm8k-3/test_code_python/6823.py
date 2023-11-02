def solution():
    """Mr. Smith had 32 markers in his classroom. He buys new boxes of markers that have 9 markers in each box. Now, he has 86 markers. How many new boxes did Mr. Smith buy?"""
    # Define the initial number of markers
    initial_markers = 32

    # Define the number of markers per box
    markers_per_box = 9

    # Define the final number of markers
    final_markers = 86

    # Calculate the number of boxes Mr. Smith bought
    boxes_bought = (final_markers - initial_markers) / markers_per_box

    # Display the number of boxes bought
    result = boxes_bought
    return result

print(solution())