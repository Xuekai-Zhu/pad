def solution():
    """Alex and his friend had a free throw contest. Alex made 8 baskets. Sandra made three times as many baskets as Alex and Hector made two times the number of baskets that Sandra made. How many baskets did they make in total?"""
    alex_baskets = 8
    sandra_baskets = 3 * alex_baskets
    hector_baskets = 2 * sandra_baskets
    total_baskets = alex_baskets + sandra_baskets + hector_baskets
    result = total_baskets
    return result

print(solution())