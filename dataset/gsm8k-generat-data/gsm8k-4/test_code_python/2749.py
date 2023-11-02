def solution():
    """Alex and his friend had a free throw contest. Alex made 8 baskets. Sandra made three times as many baskets as Alex and Hector made two times the number of baskets that Sandra made. How many baskets did they make in total?"""
    # Define the number of baskets Alex made
    alex_baskets = 8

    # Define the number of baskets Sandra made (3 times as many as Alex)
    sandra_baskets = 3 * alex_baskets

    # Define the number of baskets Hector made (2 times as many as Sandra)
    hector_baskets = 2 * sandra_baskets

    # Calculate the total number of baskets made
    total_baskets = alex_baskets + sandra_baskets + hector_baskets

    # return the result
    result = total_baskets
    return result

print(solution())