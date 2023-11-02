def solution():
    # Convert 7 dozen oranges to total number of oranges
    total_oranges = 7 * 12

    # Calculate how many oranges were reserved for his friend
    friend_oranges = total_oranges * (1/4)

    # Calculate how many oranges are remaining after reserving for his friend
    remaining_oranges = total_oranges - friend_oranges

    # Calculate how many oranges were sold yesterday
    sold_yesterday = remaining_oranges * (3/7)

    # Calculate how many oranges are left after selling yesterday and the four rotten ones
    left_to_sell = remaining_oranges - sold_yesterday - 4

    result = left_to_sell
    return result

print(solution())