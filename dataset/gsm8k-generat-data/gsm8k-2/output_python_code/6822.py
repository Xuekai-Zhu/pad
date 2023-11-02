def solution():
    """Mr. Smith had 32 markers in his classroom. He buys new boxes of markers that have 9 markers in each box. Now, he has 86 markers. How many new boxes did Mr. Smith buy?"""
    starting_markers = 32
    total_markers = 86
    markers_bought = total_markers - starting_markers
    markers_per_box = 9
    boxes_bought = markers_bought // markers_per_box
    result = boxes_bought
    return result

print(solution())