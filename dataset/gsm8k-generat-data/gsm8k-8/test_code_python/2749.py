def solution():
    # Define the number of baskets made by Alex, Sandra, and Hector
    alex_baskets = 8
    sandra_baskets = 3 * alex_baskets
    hector_baskets = 2 * sandra_baskets

    # Calculate the total number of baskets made
    total_baskets = alex_baskets + sandra_baskets + hector_baskets
    result = total_baskets
    return result

print(solution())