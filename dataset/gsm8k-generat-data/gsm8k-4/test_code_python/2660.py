def solution():
    """Mr. Salazar had seven dozen oranges. He reserved 1/4 of it for his friend and was able to sell 3/7 of the remaining yesterday. Today, he saw four rotten oranges. How many oranges are left to be sold today?"""
    # Define the initial number of oranges
    initial_oranges = 7 * 12

    # Calculate the number of oranges reserved for his friend
    friend_oranges = initial_oranges * (1/4)

    # Calculate the number of oranges remaining after reserving for his friend
    remaining_oranges = initial_oranges - friend_oranges

    # Calculate the number of oranges sold yesterday
    sold_oranges = remaining_oranges * (3/7)

    # Calculate the number of oranges left today after 4 are found to be rotten
    left_oranges = remaining_oranges - sold_oranges - 4

    # return the result
    result = left_oranges
    return result

print(solution())