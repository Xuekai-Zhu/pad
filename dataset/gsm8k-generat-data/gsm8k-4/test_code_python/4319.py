def solution():
    """Tammy has 10 orange trees from which she can pick 12 oranges each day. Tammy sells 6-packs of oranges for $2. How much money will Tammy have earned after 3 weeks if she sells all her oranges?"""
    # Define the number of orange trees and oranges per day
    ORANGE_TREES = 10
    ORANGES_PER_DAY = 12

    # Define the number of days in 3 weeks
    DAYS_3_WEEKS = 21

    # Calculate the total number of oranges Tammy can pick in 3 weeks
    total_oranges = ORANGE_TREES * ORANGES_PER_DAY * DAYS_3_WEEKS

    # Calculate the number of 6-packs Tammy can make with her oranges
    num_6packs = total_oranges // 6

    # Calculate the total earnings from selling 6-packs
    total_earnings = num_6packs * 2

    return total_earnings

print(solution())