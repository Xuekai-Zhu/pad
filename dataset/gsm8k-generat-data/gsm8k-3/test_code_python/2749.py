def solution():
    """Alex and his friend had a free throw contest. Alex made 8 baskets. Sandra made three times as many baskets as Alex and Hector made two times the number of baskets that Sandra made. How many baskets did they make in total?"""
    # Number of baskets Alex made
    alex_baskets = 8

    # Number of baskets Sandra made
    sandra_baskets = 3 * alex_baskets

    # Number of baskets Hector made
    hector_baskets = 2 * sandra_baskets

    # Total number of baskets made
    total_baskets = alex_baskets + sandra_baskets + hector_baskets

    # Display the total number of baskets
    result = total_baskets
    return result

print(solution())