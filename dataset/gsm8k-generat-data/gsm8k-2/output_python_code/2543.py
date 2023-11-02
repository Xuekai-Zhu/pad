def solution():
    """Michael’s largest watermelon weighs 8 pounds. His neighbor, Clay, grew a watermelon three times that size. And their mutual friend, John, grew a watermelon that was half the size of Clay’s. How big was John’s watermelon?"""
    michael_watermelon = 8
    clay_watermelon = 3 * michael_watermelon
    john_watermelon = 0.5 * clay_watermelon
    result = john_watermelon
    return result

print(solution())