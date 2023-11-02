def solution():
    """Michael’s largest watermelon weighs 8 pounds. His neighbor, Clay, grew a watermelon three times that size. And their mutual friend, John, grew a watermelon that was half the size of Clay’s. How big was John’s watermelon?"""
    michael_watermelon = 8
    clay_watermelon = michael_watermelon * 3
    john_watermelon = clay_watermelon / 2
    result = john_watermelon
    return result

print(solution())