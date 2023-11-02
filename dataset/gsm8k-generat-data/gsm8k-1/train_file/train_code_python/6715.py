def solution():
    """TreShaun's full marker has enough ink in it to paint three 4 inch by 4 inch squares. If he colors in two 6 inch by 2 inch rectangles, what percentage of ink is left?"""
    # One 4x4 square is 16 sq. inches
    ink_per_square = 16
    
    # TreShaun colored in two 6x2 rectangles, which is 12 sq. inches each
    ink_used = 24
    
    # TreShaun started with enough ink for three squares, so he had 48 sq. inches of ink
    starting_ink = 48
    
    # Calculate the percentage of ink remaining
    ink_remaining = starting_ink - ink_used
    percentage_remaining = (ink_remaining / starting_ink) * 100
    
    result = percentage_remaining
    return result

print(solution())