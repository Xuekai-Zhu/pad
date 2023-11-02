def solution():
    """
    There were sweets on the table. Jack came and took half of all the candies and 4 more candies. 
    Then Paul came and took the remaining 7 sweets. How many sweets were on the table at first?
    """
    # Let's assume there were 'x' sweets on the table at first
    # Jack took half of the sweets and 4 more candies
    x_after_jack = (x / 2) - 4

    # Paul took the remaining sweets, which is (x/2) - 4, leaving 7 sweets behind
    x = (x / 2) - 4 + 7

    # Solving for x
    x = (2 * x) - 6

    # Display the initial number of sweets on the table
    result = x
    return result

print(solution())