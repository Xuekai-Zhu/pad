def solution():
    """TreShaun's full marker has enough ink in it to paint three 4 inch by 4 inch squares. If he colors in two 6 inch by 2 inch rectangles, what percentage of ink is left?"""
    total_available_ink = 3
    ink_used_for_rectangles = (6*2*2) * 2
    ink_left = total_available_ink - (ink_used_for_rectangles/16)
    ink_percentage_left = ink_left / total_available_ink * 100
    result = ink_percentage_left
    return result

print(solution())