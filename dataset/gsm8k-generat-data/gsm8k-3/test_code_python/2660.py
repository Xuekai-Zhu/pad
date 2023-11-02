def solution():
    """Mr. Salazar had seven dozen oranges. He reserved 1/4 of it for his friend and was able to sell 3/7 of the remaining 
    yesterday. Today, he saw four rotten oranges. How many oranges are left to be sold today?"""
    # Define the number of oranges in one dozen
    ORANGES_PER_DOZEN = 12

    # Define the initial number of oranges
    total_oranges = 7 * ORANGES_PER_DOZEN

    # Calculate the number of oranges reserved for his friend
    friend_oranges = total_oranges * (1/4)

    # Calculate the remaining oranges
    remaining_oranges = total_oranges - friend_oranges

    # Calculate the number of oranges sold yesterday
    sold_yesterday = remaining_oranges * (3/7)

    # Calculate the number of oranges left to be sold today
    oranges_left = remaining_oranges - sold_yesterday - 4

    # Display the number of oranges left to be sold
    result = oranges_left
    return result

print(solution())