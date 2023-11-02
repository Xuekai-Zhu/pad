def solution():
    """Henley bought 300 candies and shared them with her two brothers. However, they realized 40% of them were sour, and they had to separate those out. If they then shared the good candies equally, how many candies did each get?"""
    total_candies = 300
    sour_candies_percentage = 40
    good_candies = total_candies * (100 - sour_candies_percentage) / 100
    candies_each = good_candies / 3
    result = candies_each
    return result

print(solution())